To accomplish the task, we need to delegate this specific piece of work to our Platform Content Adapter using the `delegate_work_to_coworker` function.

Here is the JSON for the `delegate_work_to_coworker` function call with its proper arguments:

{"name": "delegate_work_to_coworker", 
"parameters": {
    "task": "Adapt the generated social media content and A/B variants into platform-optimized versions for LinkedIn, Instagram, TikTok, Facebook, and YouTube.",
    "context": "
Current Task: Adapt the generated social media content and A/B variants into platform-optimized versions for LinkedIn, Instagram, TikTok, Facebook, and YouTube.
You must: - Adjust tone for each platform (professional vs casual vs viral) - Reformat structure (line breaks, emojis, captions, hooks) - Add platform-specific hashtag strategies - Optimize for algorithm behavior (retention, engagement, watch time) - Ensure each platform version feels native, not copied
Use inputs from: - write_copy (base posts) - ab_variant_task (hook variations) - campaign_develpoment (strategy and positioning)
Think like a growth marketer optimizing the same message across 5 algorithms.
This is the expected criteria for your final answer: A platform-specific content package including:
LinkedIn: - 1-2 professional, insight-driven posts - Minimal hashtags, strong storytelling or authority tone
Instagram: - Highly engaging caption formats - Emoji usage + hashtag clusters - Short-form viral-friendly structure
TikTok: - Hook-first scripts - Short punchy captions - Retention-optimized phrasing
Facebook: - Conversational, community-driven tone - Story-heavy formatting
YouTube (Shorts or Community): - Title-style hooks - Engagement-driven phrasing
Each platform section must clearly show: - Adapted post - Hook variant used - Why it fits the platform.",
    "coworker": "Platform Content Adapter"
}}