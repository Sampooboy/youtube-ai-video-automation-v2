# YouTube AI Video Automation v2

A project that helps prepare YouTube Shorts using an automated workflow:

**Topic → Scene Planning → Google Flow → Exported Video Scenes → FFmpeg Assembly**

## Workflow Overview

1. **Topic Input**: Provide a topic in `input/topic.txt`
2. **Scene Planning**: Generate 10-second vertical scene prompts tailored for YouTube Shorts (9:16 aspect ratio)
3. **Google Flow**: Use the exported prompts with Google Flow (external tool) to create video scenes
4. **Export & Assembly**: Collect the rendered video scenes and prepare them for FFmpeg assembly (future step)

## Project Structure

```
youtube-ai-video-automation-v2/
├── README.md
├── .gitignore
├── input/
│   └── topic.txt
├── scripts/
│   └── make_project.py
├── prompts/
│   └── flow_prompt_template.md
├── assets/
│   └── .gitkeep
├── projects/
│   └── .gitkeep
└── output/
    └── .gitkeep
```

## Getting Started

1. Update `input/topic.txt` with your YouTube Shorts topic
2. Run `python scripts/make_project.py`
3. Review the generated project folder in `projects/`
4. Use the scene prompts with Google Flow to generate video content
5. Collect exported videos for FFmpeg assembly

## Notes

- **Google Flow** is an external tool used for video scene generation
- This project handles planning and prompt generation
- FFmpeg integration for final video assembly is planned for a future step
- No API keys, tokens, or external credentials are required for this phase
- Uses Python standard library only
