# accio
 
 Another way of installing one or more tools based on different criteria such as:
 - the tools name
 - the tools language
 - the tools tags (e.g. "recon", "project_discovery", "tomnomnom")

exmaple usage: Install all tools written in python
> accio --language python
 
exmaple usage: Install all tools tagged with "recon"
> accio --tag recon

exmaple usage: Install all tools tagged with "recon" and "project_discovery"
> accio --tag recon --tag project_discovery

exmaple usage: Install all tools
>  accio --all

exmaple usage: Install specific tool
>  accio --tool subfinder


TODO:
- Update pull down/refresh json or create external public dataset
- Add option to use https://lobuhi.github.io/?# dataset
- Update install for python tools to use pyenv and create simlink in /usr/local/bin/
- Support for confg files & API Tokens
- Support for wordlists
- Support for containers
- Consider creating application in go
