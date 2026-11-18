---
title: agent-framework
url: https://pypi.org/project/agent-framework/
hostname: pypi.org
description: Microsoft Agent Framework for building AI Agents with Python. This package contains core and a curated set of optional integrations.
sitename: PyPI
date: "2026-11-12"
fingerprint: "8412ae5ae8b6b002"
---
# Get Started with Microsoft Agent Framework for Python Developers

## Quick Install

We recommend two common installation paths depending on your use case.

### 1. Development mode

If you are exploring or developing locally, install the standard framework package set:

```
pip install agent-framework
```
This installs the core and the standard integration packages. Experimental Lab modules are installed separately
with `pip install agent-framework-lab`.

### 2. Selective install

If you only need specific integrations, you can install at a more granular level. This keeps dependencies lighter and focuses on what you actually plan to use. Some examples:

```
# Core only
# includes Azure OpenAI and OpenAI support by default
# also includes workflows and orchestrations
pip install agent-framework-core
# Core + Microsoft Foundry integration
pip install agent-framework-foundry
# Core + Microsoft Copilot Studio integration (preview package)
pip install agent-framework-copilotstudio --pre
# Core + both Microsoft Copilot Studio and Microsoft Foundry integration
pip install --pre agent-framework-copilotstudio agent-framework-foundry
```
This selective approach is useful when you know which integrations you need, and it is the recommended way to set up lightweight environments. Released packages such as `agent-framework`, `agent-framework-core`, and `agent-framework-foundry` no longer require `--pre`, while preview connectors such as `agent-framework-copilotstudio` still do.

Supported Platforms:

- Python: 3.11–3.15
- OS: Windows, macOS, Linux

Python 3.11 or later is required. Supported environments are subject to the integration-specific limits below.

### Python 3.15 limitations

`pip install agent-framework` resolves and imports on Python 3.15, but it does
not provide exactly the same feature set as Python 3.14:

| Area | Python 3.15 impact | 
|---|---|
| Declarative Power Fx | `agent-framework-declarative` is installed, but its `powerfx` dependency is not. YAML values beginning with `=` produce a warning and remain unchanged instead of being evaluated. Declarative agents or workflows that rely on expressions may therefore use invalid literal values or fail later. | 

## 1. Setup API Keys

Set as environment variables, or create a .env file at your project root:

```
OPENAI_API_KEY=sk-...
OPENAI_MODEL=...
...
AZURE_OPENAI_API_KEY=...
AZURE_OPENAI_ENDPOINT=...
AZURE_OPENAI_MODEL=...
...
FOUNDRY_PROJECT_ENDPOINT=...
FOUNDRY_MODEL=...
```
For the generic OpenAI clients (`OpenAIChatClient` and `OpenAIChatCompletionClient`), configuration
resolves in this order:

1. Explicit Azure inputs such as `credential` or `azure_endpoint`
2. `OPENAI_API_KEY` / explicit OpenAI API-key parameters
3. Azure environment fallback such as `AZURE_OPENAI_ENDPOINT` and `AZURE_OPENAI_API_KEY`

This means mixed shells default to OpenAI when `OPENAI_API_KEY` is present. To force Azure routing,
pass an explicit Azure input such as `credential=AzureCliCredential()`.

You can also override environment variables by explicitly passing configuration parameters to the chat client constructor:

```
from agent_framework.openai import OpenAIChatClient
client = OpenAIChatClient(
    api_key='',
    azure_endpoint='',
    model='',
    api_version='',
)
```
See the following [setup guide](https://pypi.org/samples/01-get-started) for more information.

## 2. Create a Simple Agent

Create agents and invoke them directly:

```
import asyncio
from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient
async def main():
    agent = Agent(
        client=OpenAIChatClient(),
        instructions="""
        1) A robot may not injure a human being...
        2) A robot must obey orders given it by human beings...
        3) A robot must protect its own existence...
        Give me the TLDR in exactly 5 words.
        """
    )
    result = await agent.run("Summarize the Three Laws of Robotics")
    print(result)
asyncio.run(main())
# Output: Protect humans, obey, self-preserve, prioritized.
```
## 3. Directly Use Chat Clients (No Agent Required)

You can use the chat client classes directly for advanced workflows:

```
import asyncio
from agent_framework import Message
from agent_framework.openai import OpenAIChatClient
async def main():
    client = OpenAIChatClient()
    messages = [
        Message("system", ["You are a helpful assistant."]),
        Message("user", ["Write a haiku about Agent Framework."])
    ]
    response = await client.get_response(messages)
    print(response.messages[0].text)
    """
    Output:
    Agents work in sync,
    Framework threads through each task—
    Code sparks collaboration.
    """
asyncio.run(main())
```
### Connection and credential lifetimes

Chat clients support async context managers for deterministic cleanup:

```
from agent_framework import Agent, Message
from agent_framework.openai import OpenAIChatClient
async with OpenAIChatClient() as client:
    response = await client.get_response([Message("user", ["Hello!"])])
# Alternatively, let the agent enter and exit its chat client's context.
async with Agent(client=OpenAIChatClient(), instructions="Be helpful.") as agent:
    response = await agent.run("Hello!")
```
Calling clients without a context manager remains supported; use `await client.close()` when finished.
Context exit releases connections created by the connector, including on exceptions. Caller-supplied SDK clients,
HTTP transports, and credentials remain caller-owned. In particular, closing an Azure SDK connection does not
close the credential supplied to it. Scope credentials outside the agent or client that uses them:

```
from azure.identity.aio import AzureCliCredential
async with AzureCliCredential() as credential:
    async with OpenAIChatClient(
        azure_endpoint="https://YOUR-RESOURCE.openai.azure.com",
        model="YOUR-DEPLOYMENT",
        credential=credential,
    ) as client:
        response = await client.get_response([Message("user", ["Hello!"])])
```
Treat closing a resource-owning client as the end of its lifetime; reopening is SDK-dependent. Avoid overlapping
agent contexts sharing a connector-owned connection, since exiting either agent closes that connection. To share
an SDK client across agents, inject it into their chat clients and manage its lifetime outside those agent contexts.
`BaseChatClient` provides default context methods and a no-op `close()`, so custom subclasses do not need to
implement lifecycle methods unless they own resources. Protocol-only chat clients do not need context methods.
Inherited context exit also supports existing subclasses whose `close()` is synchronous.

## 4. Build an Agent with Tools and Functions

Enhance your agent with custom tools and function calling:

```
import asyncio
from typing import Annotated
from random import randint
from pydantic import Field
from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient
def get_weather(
    location: Annotated[str, Field(description="The location to get the weather for.")],
) -> str:
    """Get the weather for a given location."""
    conditions = ["sunny", "cloudy", "rainy", "stormy"]
    return f"The weather in {location} is {conditions[randint(0, 3)]} with a high of {randint(10, 30)}°C."
def get_menu_specials() -> str:
    """Get today's menu specials."""
    return """
    Special Soup: Clam Chowder
    Special Salad: Cobb Salad
    Special Drink: Chai Tea
    """
async def main():
    agent = Agent(
        client=OpenAIChatClient(),
        instructions="You are a helpful assistant that can provide weather and restaurant information.",
        tools=[get_weather, get_menu_specials]
    )
    response = await agent.run("What's the weather in Amsterdam and what are today's specials?")
    print(response)
    """
    Output:
    The weather in Amsterdam is sunny with a high of 22°C. Today's specials include
    Clam Chowder soup, Cobb Salad, and Chai Tea as the special drink.
    """
if __name__ == "__main__":
    asyncio.run(main())
```
You can explore additional agent samples [here](https://pypi.org/samples/02-agents).

## 5. Multi-Agent Orchestration

Coordinate multiple agents to collaborate on complex tasks using orchestration patterns:

```
import asyncio
from agent_framework import Agent
from agent_framework.openai import OpenAIChatClient
async def main():
    # Create specialized agents
    writer = Agent(
        client=OpenAIChatClient(),
        name="Writer",
        instructions="You are a creative content writer. Generate and refine slogans based on feedback."
    )
    reviewer = Agent(
        client=OpenAIChatClient(),
        name="Reviewer",
        instructions="You are a critical reviewer. Provide detailed feedback on proposed slogans."
    )
    # Sequential workflow: Writer creates, Reviewer provides feedback
    task = "Create a slogan for a new electric SUV that is affordable and fun to drive."
    # Step 1: Writer creates initial slogan
    initial_result = await writer.run(task)
    print(f"Writer: {initial_result}")
    # Step 2: Reviewer provides feedback
    feedback_request = f"Please review this slogan: {initial_result}"
    feedback = await reviewer.run(feedback_request)
    print(f"Reviewer: {feedback}")
    # Step 3: Writer refines based on feedback
    refinement_request = f"Please refine this slogan based on the feedback: {initial_result}\nFeedback: {feedback}"
    final_result = await writer.run(refinement_request)
    print(f"Final Slogan: {final_result}")
    # Example Output:
    # Writer: "Charge Forward: Affordable Adventure Awaits!"
    # Reviewer: "Good energy, but 'Charge Forward' is overused in EV marketing..."
    # Final Slogan: "Power Up Your Adventure: Premium Feel, Smart Price!"
if __name__ == "__main__":
    asyncio.run(main())
```
For more advanced orchestration patterns including Sequential, Concurrent, Group Chat, Handoff, and Magentic orchestrations, see the [orchestration samples](https://pypi.org/samples/03-workflows/orchestrations).

## More Examples & Samples

- [Getting Started with Agents](https://pypi.org/samples/02-agents): Basic agent creation and tool usage
- [Chat Client Examples](https://pypi.org/samples/02-agents/chat_client): Direct chat client usage patterns
- [Foundry Integration](https://github.com/microsoft/agent-framework/tree/main/python/packages/foundry): Microsoft Foundry integration
- [Workflow Samples](https://pypi.org/samples/03-workflows): Advanced multi-agent patterns

## Agent Framework Documentation

## Metadata

## Release files for agent-framework 1.26.0

For a detailed explanation of source distributions (sdists) and built distributions (wheels), please see the [package formats documentation](https://packaging.python.org/en/latest/discussions/package-formats/#package-formats).

### Source distribution (sdist)

| Source distribution for agent-framework 1.26.0 |  |  |  |  | 
|---|---|---|---|---|
| File | Size | Uploaded | Provenance | Actions | 
|---|---|---|---|---|
|  [agent\_framework-1.26.0.tar.gz](https://files.pythonhosted.org/packages/56/bf/b5bb8dc92f6b744433f67d1bb9c5d3b8b7968247e7dfe923edd0880e4459/agent_framework-1.26.0.tar.gz) | 14.3 kB |  | Without provenance | [Details for agent\_framework-1.26.0.tar.gz](https://pypi.org#agent_framework-1.26.0.tar.gz) | 

### Built distribution (wheel)

| Table of built distributions (wheels) for agent-framework 1.26.0 |  |  |  |  | 
|---|---|---|---|---|
| File | Interpreter | ABI | Platform | Actions [Reset](https://pypi.org/project/agent-framework/#files) | 
|---|---|---|---|---|
|  [agent\_framework-1.26.0-py3-none-any.whl](https://files.pythonhosted.org/packages/16/37/cfcd19bfb8db9c5e6bc7836284e61a55d77895a7aa7ddd9047b9b3db94b3/agent_framework-1.26.0-py3-none-any.whl) | Python 3 | none | any | [Details for agent\_framework-1.26.0-py3-none-any.whl](https://pypi.org#agent_framework-1.26.0-py3-none-any.whl) | 

**Total release size:** 21.0 kB

## [Release files](https://pypi.org#files)
    / agent\_framework-1.26.0.tar.gz

| Download URL |                           [agent\_framework-1.26.0.tar.gz](https://files.pythonhosted.org/packages/56/bf/b5bb8dc92f6b744433f67d1bb9c5d3b8b7968247e7dfe923edd0880e4459/agent_framework-1.26.0.tar.gz)            | 
|---|---|
| Size | 14.3 kB | 
| Tags | Source | 
| SHA-256 checksum [How to use checksums](https://pip.pypa.io/en/stable/topics/secure-installs/#hash-checking-mode) | ```              b20870b77f237bcf52b6abbab86364f7fcbb23d41d217fd0d643556d19462167                         ```  | 
| BLAKE2b-256 checksum [How to use checksums](https://pip.pypa.io/en/stable/topics/secure-installs/#hash-checking-mode) | ```              56bfb5bb8dc92f6b744433f67d1bb9c5d3b8b7968247e7dfe923edd0880e4459                         ```  | 
| Upload date |  | 
| Uploaded using Trusted Publishing? [What is trusted publishing?](https://docs.pypi.org/trusted-publishers/) | No | 
| Uploaded via | `RestSharp/106.13.0.0` | 

## [Release files](https://pypi.org#files)
    / agent\_framework-1.26.0-py3-none-any.whl

| Download URL |                           [agent\_framework-1.26.0-py3-none-any.whl](https://files.pythonhosted.org/packages/16/37/cfcd19bfb8db9c5e6bc7836284e61a55d77895a7aa7ddd9047b9b3db94b3/agent_framework-1.26.0-py3-none-any.whl)            | 
|---|---|
| Size | 6.7 kB | 
| Tags | Python 3 | 
| SHA-256 checksum [How to use checksums](https://pip.pypa.io/en/stable/topics/secure-installs/#hash-checking-mode) | ```              14267ec8e6929c139015f8ec918adc638a71c7656901413426bb30ab199b6d71                         ```  | 
| BLAKE2b-256 checksum [How to use checksums](https://pip.pypa.io/en/stable/topics/secure-installs/#hash-checking-mode) | ```              1637cfcd19bfb8db9c5e6bc7836284e61a55d77895a7aa7ddd9047b9b3db94b3                         ```  | 
| Upload date |  | 
| Uploaded using Trusted Publishing? [What is trusted publishing?](https://docs.pypi.org/trusted-publishers/) | No | 
| Uploaded via | `RestSharp/106.13.0.0` | 

## Security for agent-framework 1.26.0

### Provenance

**Provenance** describes where a file came from. On PyPI, provenance is shared via **attestations**, which provide a verifiable record of the build or publishing details. [View details, limitations and caveats.](https://docs.pypi.org/using-pypi/package-security/provenance/)

#### No provenance found

None of the files in this release were uploaded with provenance metadata.

### A note on package security

PyPI is a repository for distributing packages, not a service for auditing them. While third-party security researchers and our staff do their best to detect and remove malicious packages, PyPI cannot guarantee the quality, security or suitability of any given package.

To learn more about protecting yourself from malicious actors, visit our [package security documentation](https://docs.pypi.org/using-pypi/package-security/introduction/).
