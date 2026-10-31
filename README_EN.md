# OpenFic (LightEastDS Edition)

![GitHub Repo stars](https://img.shields.io/github/stars/LightEastDS/OpenFic)
![License](https://img.shields.io/badge/License-Apache_2.0-red)
![GitHub Release](https://img.shields.io/github/v/release/LightEastDS/OpenFic?logo=githubactions&logoColor=white&color=yellow)
![PyPI - Version](https://img.shields.io/pypi/v/openfic?logo=pypi&logoColor=white&color=green)

[中文](./README.md) | English

> [!NOTE]  
> This project is a fork of upstream [syrizelink/OpenFic](https://github.com/syrizelink/OpenFic).  
> While retaining upstream features, this edition refactors the style system for publication-grade literature, lifts rigid chapter word count constraints, disables redundant default skills, and introduces a full-stack precise Chinese word counting tool. See [FORK_DIFFERENCES.md](./FORK_DIFFERENCES.md) for details.

**OpenFic** is an all-in-one, cross-platform, AI-native writing tool built for fiction authors. It helps you build world, design characters, and shape custom workflows, so the Agent fits your writing process instead of forcing you into its own.

![Demo Screenshot](./demo.png)

## When to Use OpenFic

> [!Tip]  
> *OpenFic is designed for Agent-assisted writing, not one-click novel generation. It is first and foremost a writing tool for fiction, and then an AI Agent system built around that workflow.*

#### It works well when you:

- are writing a mid-length or long-form novel and need to keep track of worldbuilding, characters, foreshadowing, and chapter details
- want an Agent to help with brainstorming, continuity checks, and detail expansion
- already have your own setting, tone, and plot direction, and want help turning ideas into actual prose
- want to customize prompts, Agents, and workflows around your own writing process
- care about local data storage, context management, and sustainable long-term collaboration

#### It is probably not a good fit when you:

- expect to type one prompt and get a complete novel automatically
- mainly need short-form marketing copy, social posts, or generic one-off text generation
- do not plan to maintain detailed project material or long-term writing context

## Features

- 🚀 **Ready out of the box**: install with Docker or pip, or use the desktop app directly, with minimal setup
- ✒️ **Built for writing**: an editor designed around fiction writing, with a comfortable long-form writing experience
- 🤝 **Broad model support**: works with many providers, including any model compatible with the OpenAI API
- 📱 **Responsive UI**: designed for desktop, mobile, and browser use without breaking the workflow
- 🧩 **Custom workflows**: a highly configurable Agent system that lets you adapt prompts and workflows to your needs
- 🤖 **Human-AI co-writing**: Agents help with brainstorming, plotting, and editing, instead of replacing the writing process with one-click generation
- 💾 **Local persistence**: all project data stays on your machine, with no cloud storage dependency
- 🧠 **Semantic retrieval**: Agentic RAG built on vector search, so Agents can retrieve information efficiently even in projects with millions of words
- ⚖️ **Cost-aware context handling**: layered context management, smart compression, dynamic truncation, and stable caching to reduce usage cost

## Quick Start

### 🐳 Docker (Recommended)

If you are self-hosting, Docker is the recommended way to run OpenFic.

```bash
docker run -d -p 8000:8000 -v "openfic:/data" --name openfic ghcr.io/syrizelink/openfic:latest
```

### 🐍 Python pip

> [!WARNING]  
> Before you start, make sure Python 3.12+ is installed.

#### 1. Install OpenFic

```bash
pip install openfic
```

#### 2. Start the server

```bash
openfic serve
```

### 🖥 Desktop App

Download the desktop app from [Release Page](https://github.com/LightEastDS/OpenFic/releases) (or upstream [Release Page](https://github.com/syrizelink/OpenFic/releases)) and run it natively on your system.

## Contributing

Contributions of any kind are welcome. If you have ideas, suggestions, or code improvements, feel free to open an Issue or submit a Pull Request.

- **Report bugs**: open an Issue with as much detail as possible
- **Suggest features**: share your ideas in Issues
- **Submit code**: fork the repository, make your changes, and open a Pull Request

See [CONTRIBUTING.md](./CONTRIBUTING.md) for detailed contribution guidelines.

## Star History

<a href="https://www.star-history.com/?repos=LightEastDS%2FOpenFic&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=LightEastDS%2FOpenFic&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=LightEastDS%2FOpenFic&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=LightEastDS%2FOpenFic&type=date&legend=top-left" />
 </picture>
</a>

## Acknowledgements

- [OpenFic (syrizelink/OpenFic)](https://github.com/syrizelink/OpenFic) - Upstream repository
- [SillyTavern](https://github.com/SillyTavern/SillyTavern) - inspiration
- [oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) - reference for the built-in writing Skill

## Community

- [LINUX DO](https://linux.do/)
- Upstream QQ Group: [1105304435](https://qun.qq.com/universal-share/share?ac=1&authKey=XxKBo33K1IAy%2FejDsGPWOn51pCNk1Bu1%2F2dtldtWCWSdPGor4tZkaboxgrGkz2BS&busi_data=eyJncm91cENvZGUiOiIxMTA1MzA0NDM1IiwidG9rZW4iOiJCY1NuV2s5d1B2QmI2R0ZiMldMbDE4MVRPV1puMFJlWjZIRlZrRjk4WGUwY2wvdUlaWEFPZ1cvV0lLbWl6d3JwIiwidWluIjoiMjUzMjEyNDQwNCJ9&data=B2VDUuvIYSScsKPwMeFB6txn6fj8I18zG6EKsmsrZDwPpmNCoJ7r5NTLtmUUf58MK3Lw9evkkPg28EglHJNONA&svctype=4&tempid=h5_group_info)

## License

[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
