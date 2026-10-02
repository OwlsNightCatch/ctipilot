---
title: OpenAI software attempted to secretly scrape data from dozens of prominent websites
author: Suzanne Smalley
url: https://therecord.media/openai-software-attempted-to-secretly-scrape-data-from-dozens-of-websites
hostname: therecord.media
description: The findings, released Thursday by Asymmetric Security, are just the latest example of rogue behavior spurred by OpenAI’s software.
sitename: The Record
date: "2026-10-01"
---
# OpenAI software attempted to secretly scrape data from dozens of prominent websites

OpenAI agents scraped data from more than 50 private and public sector organizations’ websites over a six-month period earlier this year.

The findings, released Thursday by Asymmetric Security, are just the latest example of rogue behavior spurred by OpenAI’s software. They come amid mounting concerns about the increasing dangers posed by the technology.

 Asymmetric, a digital forensics startup backed by top technology venture capitalists and co-founded by [experts](https://www.linkedin.com/posts/zamajid_today-with-pippa-thompson-and-alexis-carlier-share-7419856562946473984-rB8H/) from Crowdstrike, RAND, Palo Alto Networks and Stanford, said it launched its investigation just days ago following reports that the OpenAI’s agents hacked the Australian government and the U.S. Department of Education.  

 The rogue agents accessed data from 55 targeted websites, including the FBI’s crime data explorer, the Centers for Disease Control and Prevention (CDC), the International Energy Agency and the Mayo Clinic, Asymmetric said in a Monday [blog post](https://www.asymmetricsecurity.com/newsroom/rogue-agents-investigation-initial-findings/) describing initial findings.  

Most of the data collected by the agents is public, the blog post said. The time frame the researchers studied spanned from March to September 20.

 “The activity extended beyond searching for information,” Asymmetric said in a far more detailed Thursday [post](https://www.asymmetricsecurity.com/newsroom/rogue-agents-investigation/). “The records show attempts to find exposed configuration files, create accounts, route requests through third-party services and retrieve results through unintended channels.” 

The methods used were sophisticated, according to the researchers, who said they found evidence showing the AI software used out-of-the-box tactics to erase records of the activity, making it impossible to know if the software accessed “sensitive data based on public information alone,” according to the blog post.

The agents successfully accessed staging environments and used attacker reconnaissance strategies, Asymmetry said.

The novel methods allowed the agents to “gain full web access despite the constraints of their sandbox,” according to the blog post.

The agents created accounts with browser platforms, burner emails and scanning services in an effort to receive registration and verification emails. Scanning services were deployed to unlock more features, the blog post said.

The agents appeared to have been assigned to research public health data, the blog post said, noting that they surfaced evidence of searches for health and prescription statistics from the Australian Institute of Health and Welfare and “trade figures” from the UN’s Trade and Development Body (UNCTAD).

The software created the burner email inboxes using Urlquery, which is typically deployed to search for malware on websites. From there, the agents downloaded the data.

The agents’ methods are similar to techniques used by human hackers, Asymmetry co-founder Pippa Thompson told the Financial Times.

 “It’s possible that the agents were deliberately using these tools to cover their tracks,” she reportedly said. OpenAI did not immediately respond to a request for comment, but [told](https://www.ft.com/content/11502a49-5319-4df5-95ea-2d76669c31a6?syn-25a6b1a6=1) the Financial Times it is investigating and noted that much of the activity the Asymmetry team found involved “routine research tasks” relying on publicly available information. 

No external experts have thus far confirmed Asymmetric’s findings.

The researchers relied solely on publicly available data, the blog post said, but they did not provide additional detail regarding how they reached their conclusions.

 On Monday, OpenAI apologized to the Australian government for its software’s hack of Australia’s Medicare health program, which nearly everyone on the continent uses and shares data with. OpenAI did not publicize the attack — which it learned of in mid-August — until after the country’s prime minister [disclosed](https://therecord.media/openai-apologizes-australia-medicare-breach) it to reporters. The data the agents accessed included non-public information. 

 In July, OpenAI acknowledged its models were responsible for the June hack of the AI platform [Hugging Face](https://therecord.media/openai-apologizes-australia-medicare-breach). The company did not confirm the incident until five days after Hugging Face made the incident public, saying they discovered an autonomous agent launched an “end-to-end attack.” 


Suzanne Smalley

is a reporter covering digital privacy, surveillance technologies and cybersecurity policy for The Record. She was previously a cybersecurity reporter at CyberScoop. Earlier in her career Suzanne covered the Boston Police Department for the Boston Globe and two presidential campaign cycles for Newsweek. She lives in Washington with her husband and three children.
