import yaml,sys,re
def fmt(d):
    return yaml.safe_dump(d,default_flow_style=True,width=10**9,allow_unicode=True,sort_keys=False).strip()
def block(n,model,model_id,start,end,dur,verdict,truth,editorial,advisory,cin,cchk,findings):
    out=f"""    - n: {n}
      model: {model}
      model_id: {model_id}
      subagent_type: cti-verification
      started_at: '{start}'
      ended_at: '{end}'
      duration_seconds: {dur}
      verdict: {verdict}
      truth: {truth}
      editorial: {editorial}
      advisory: {advisory}
      claims_in_scope: {cin}
      claims_checked: {cchk}
      findings:
"""
    for f in findings: out+="        - "+fmt(f)+"\n"
    return out
def append(p,text):
    s=open(p).read()
    if "  iterations: []" in s:
        s=s.replace("  iterations: []","  iterations:\n"+text.rstrip('\n'),1)
    else:
        marker="\n---\n\n## Verification & coverage notes"
        assert marker in s
        s=s.replace(marker,"\n"+text.rstrip('\n')+marker,1)
    open(p,'w').write(s)
