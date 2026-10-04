#!/usr/bin/env python3
"""
YouTube AI Video Automation - Project Generator

This script reads a topic from input/topic.txt and generates a project folder
with timestamped naming, containing scene prompts for Google Flow.
"""

import json
import os
from datetime import datetime


def read_topic():
    """Read topic from input/topic.txt."""
    topic_file = "input/topic.txt"
    if not os.path.exists(topic_file):
        print(f"Error: {topic_file} not found")
        return None

    with open(topic_file, "r", encoding="utf-8") as f:
        topic = f.read().strip()

    if not topic:
        print("Error: topic.txt is empty")
        return None

    return topic


def create_project_folder():
    """Create a timestamped project folder."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    project_name = f"project_{timestamp}"
    project_path = os.path.join("projects", project_name)

    os.makedirs(project_path, exist_ok=True)
    os.makedirs(os.path.join(project_path, "assets"), exist_ok=True)

    return project_path, project_name, timestamp


def create_manifest(project_path, topic, project_name, timestamp):
    """Create manifest.json with project metadata."""
    manifest = {
        "project_name": project_name,
        "topic": topic,
        "created_at": timestamp,
        "aspect_ratio": "9:16",
        "scene_duration_seconds": 10,
        "scene_count": 6,
        "status": "prompts_generated",
    }

    manifest_path = os.path.join(project_path, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2)

    return manifest_path


def generate_scene_prompts(topic):
    """Generate 6 scene prompts for 10-second YouTube Shorts."""
    scenes = [
        {
            "scene_number": 1,
            "title": "Hook - The Problem",
            "description": f"Close-up of the main character looking directly into the camera with a concerned expression. The topic '{topic}' appears as a subtle headline on screen. Environment: modern bedroom with soft blue lighting. Character remains calm and curious.",
            "character_consistency": "Same main character in every scene",
            "environment": "Modern bedroom, minimalist and intimate",
            "action": "Direct eye contact, slight head tilt, concerned expression",
            "camera_movement": "Static shot, gentle zoom in",
            "lighting": "Soft blue mood lighting, clean and focused",
            "audio_voice_notes": "Calm but intriguing voice-over intro",
            "negative_instructions": "No watermark, no random text, no cluttered background",
        },
        {
            "scene_number": 2,
            "title": "The Pattern Appears",
            "description": "Character sits at a desk or in a cozy chair, explaining the first reason behind the scrolling habit. Subtle motion graphics of screen notifications and a scrolling app interface appear.",
            "character_consistency": "Same main character in every scene",
            "environment": "Office or bedroom desk setup",
            "action": "Natural hand gestures, thoughtful explanation",
            "camera_movement": "Slow tracking shot",
            "lighting": "Bright but soft daylight or warm lamp light",
            "audio_voice_notes": "Clear educational tone with steady pacing",
            "negative_instructions": "No watermark, no random text, no distracting background",
        },
        {
            "scene_number": 3,
            "title": "Why It Feels Addictive",
            "description": "The character moves to a living-room or simple indoor setting to explain how the brain responds to repeated notifications and quick rewards. Visual cues show a short, satisfying loop.",
            "character_consistency": "Same main character in every scene",
            "environment": "Cozy living room or modern studio setup",
            "action": "Explaining with hand movements and focused expression",
            "camera_movement": "Slight side-to-side pan",
            "lighting": "Warm ambient lighting with soft contrast",
            "audio_voice_notes": "Slightly more energetic, still easy to follow",
            "negative_instructions": "No watermark, no random text, no visual noise",
        },
        {
            "scene_number": 4,
            "title": "The Hidden Triggers",
            "description": "Character remains consistent in style and returns to the original room or environment to highlight the deeper trigger: stress, boredom, or reward loops. A subtle visual cue shows the brain reacting to constant input.",
            "character_consistency": "Same main character in every scene",
            "environment": "Bedroom or calm background with minimal distractions",
            "action": "Thoughtful pause, leaning forward, expressive gesture",
            "camera_movement": "Static close-up or slight push-in",
            "lighting": "Soft neutral lighting, intimate and focused",
            "audio_voice_notes": "Measured and reflective tone",
            "negative_instructions": "No watermark, no random text, no abrupt visual jumps",
        },
        {
            "scene_number": 5,
            "title": "A Better Way Forward",
            "description": "The character shifts into a reassuring, solution-oriented mood. They explain a healthier alternative to endless scrolling without sounding preachy. Light positive motion graphics support the idea.",
            "character_consistency": "Same main character in every scene",
            "environment": "Office, desk, or minimal creative workspace",
            "action": "Confident posture, direct but calming presentation",
            "camera_movement": "Medium shot with gentle push-in",
            "lighting": "Bright, optimistic, clean lighting",
            "audio_voice_notes": "Encouraging and motivating tone",
            "negative_instructions": "No watermark, no random text, no chaotic framing",
        },
        {
            "scene_number": 6,
            "title": "Call to Action",
            "description": "Final close-up of the character looking straight at the camera with a friendly smile. End on a clear, direct call to action for the viewer, with a clean and polished background.",
            "character_consistency": "Same main character in every scene",
            "environment": "Clean modern background with simple framing",
            "action": "Direct eye contact, warm smile, confident finish",
            "camera_movement": "Final gentle zoom or static close-up",
            "lighting": "Bright, polished, welcoming",
            "audio_voice_notes": "Friendly, upbeat, memorable ending",
            "negative_instructions": "No watermark, no random text, no distracting visual elements",
        },
    ]

    return scenes


def create_flow_prompts_file(project_path, topic, scenes):
    """Create flow_prompts.md with all scene prompts."""
    lines = [
        "# Google Flow Scene Prompts",
        "",
        f"Topic: {topic}",
        "Total Scenes: 6",
        "Duration per Scene: 10 seconds",
        "Aspect Ratio: 9:16",
        "",
        "---",
        "",
    ]

    for scene in scenes:
        lines.extend([
            f"## Scene {scene['scene_number']}: {scene['title']}",
            "",
            "Description:",
            scene["description"],
            "",
            f"Character Consistency: {scene['character_consistency']}",
            "",
            f"Environment: {scene['environment']}",
            "",
            f"Action: {scene['action']}",
            "",
            f"Camera Movement: {scene['camera_movement']}",
            "",
            f"Lighting: {scene['lighting']}",
            "",
            f"Audio/Voice Notes: {scene['audio_voice_notes']}",
            "",
            f"Negative Instructions: {scene['negative_instructions']}",
            "",
            "---",
            "",
        ])

    flow_prompts_path = os.path.join(project_path, "flow_prompts.md")
    with open(flow_prompts_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return flow_prompts_path


def main():
    """Main function to orchestrate project creation."""
    print("YouTube AI Video Automation - Project Generator")
    print("=" * 50)

    topic = read_topic()
    if not topic:
        return

    print(f"Topic loaded: {topic}")

    project_path, project_name, timestamp = create_project_folder()
    print(f"Project folder created: {project_path}")

    create_manifest(project_path, topic, project_name, timestamp)

    scenes = generate_scene_prompts(topic)
    flow_prompts_path = create_flow_prompts_file(project_path, topic, scenes)
    print(f"Scene prompts written to: {flow_prompts_path}")

    print("\nProject generated successfully.")
    print(f"Location: {project_path}")


if __name__ == "__main__":
    main()
