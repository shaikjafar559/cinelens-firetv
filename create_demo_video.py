"""
CineLens AI - Video Generator
Generates a 1080p demo video (cinelens_demo.mp4) showcasing the Fire TV app,
Amazon Bedrock integration, and AWS architecture.
"""

import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

VIDEO_WIDTH = 1920
VIDEO_HEIGHT = 1080
FPS = 30
OUTPUT_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "cinelens_demo.mp4")
ASSETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "assets")

def get_font(size, bold=False):
    # Try common Windows fonts
    font_paths = [
        "C:\\Windows\\Fonts\\segoeui.ttf",
        "C:\\Windows\\Fonts\\segoeuib.ttf" if bold else "C:\\Windows\\Fonts\\segoeui.ttf",
        "C:\\Windows\\Fonts\\arial.ttf",
        "C:\\Windows\\Fonts\\arialbd.ttf" if bold else "C:\\Windows\\Fonts\\arial.ttf"
    ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

def draw_header_footer(draw, title="CineLens AI • Fire TV & Vega OS"):
    f_title = get_font(26, bold=True)
    f_badge = get_font(20, bold=True)
    draw.rectangle([(0, 0), (VIDEO_WIDTH, 70)], fill=(11, 15, 25))
    draw.text((60, 20), title, font=f_title, fill=(248, 250, 252))
    
    # Bedrock Badge
    draw.rounded_rectangle([(VIDEO_WIDTH - 340, 16), (VIDEO_WIDTH - 60, 56)], radius=20, fill=(255, 153, 0))
    draw.text((VIDEO_WIDTH - 320, 22), "AMAZON BEDROCK", font=f_badge, fill=(0, 0, 0))

def create_title_slide(duration_sec=4.0):
    frames = []
    total_frames = int(duration_sec * FPS)
    f_huge = get_font(72, bold=True)
    f_sub = get_font(36)
    f_badge = get_font(28, bold=True)
    
    for i in range(total_frames):
        img = Image.new("RGB", (VIDEO_WIDTH, VIDEO_HEIGHT), color=(7, 9, 14))
        draw = ImageDraw.Draw(img)
        
        # Subtle glow circles
        draw.ellipse([(VIDEO_WIDTH//2 - 400, VIDEO_HEIGHT//2 - 400), (VIDEO_WIDTH//2 + 400, VIDEO_HEIGHT//2 + 400)], fill=(18, 28, 48))
        
        # Logo badge
        draw.rounded_rectangle([(VIDEO_WIDTH//2 - 70, 240), (VIDEO_WIDTH//2 + 70, 310)], radius=16, fill=(255, 153, 0))
        draw.text((VIDEO_WIDTH//2 - 20, 250), "▶", font=f_badge, fill=(0, 0, 0))
        
        # Main Title
        draw.text((VIDEO_WIDTH//2 - 260, 340), "CineLens AI", font=f_huge, fill=(248, 250, 252))
        
        # Subtitle
        draw.text((VIDEO_WIDTH//2 - 460, 450), "Intelligent Multi-Modal Viewing Companion for Fire TV & Vega OS", font=f_sub, fill=(56, 189, 248))
        draw.text((VIDEO_WIDTH//2 - 380, 520), "Next-Generation Living Room Intelligence Powered by Amazon Bedrock", font=f_sub, fill=(148, 163, 184))
        
        # Track Badges
        badges = ["Fire TV Track", "AWS Builder Challenge", "Open Source Challenge"]
        start_x = VIDEO_WIDTH//2 - 420
        for b in badges:
            draw.rounded_rectangle([(start_x, 640), (start_x + 260, 700)], radius=30, fill=(30, 41, 59), outline=(255, 153, 0), width=2)
            draw.text((start_x + 25, 655), b, font=f_badge, fill=(255, 255, 255))
            start_x += 290
            
        frames.append(cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR))
    return frames

def create_problem_slide(duration_sec=4.0):
    frames = []
    total_frames = int(duration_sec * FPS)
    f_title = get_font(48, bold=True)
    f_bullet = get_font(32)
    
    for i in range(total_frames):
        img = Image.new("RGB", (VIDEO_WIDTH, VIDEO_HEIGHT), color=(7, 9, 14))
        draw = ImageDraw.Draw(img)
        draw_header_footer(draw, "The Problem • Friction in Living Room Viewing")
        
        draw.text((120, 160), "Every Viewer Faces the Same Friction Today:", font=f_title, fill=(255, 153, 0))
        
        bullets = [
            ("🎭 Actor Confusion:", "'Wait, who is that character again and what happened in Season 1?'"),
            ("💬 Whispered Dialogue:", "'What did they just whisper? Did I miss a major plot turn?'"),
            ("⏪ Walking Away for 10 Mins:", "'Can someone catch me up without spoiling the rest of the movie?'"),
            ("✨ Static Trivia Limits:", "Prime Video X-Ray was a pioneer, but static cards cannot answer conversational questions.")
        ]
        
        y = 270
        for b_title, b_desc in bullets:
            draw.rounded_rectangle([(120, y), (VIDEO_WIDTH - 120, y + 100)], radius=16, fill=(18, 24, 38), outline=(51, 65, 85), width=1)
            draw.text((150, y + 18), b_title, font=f_bullet, fill=(56, 189, 248))
            draw.text((150, y + 55), b_desc, font=f_bullet, fill=(226, 232, 240))
            y += 125
            
        frames.append(cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR))
    return frames

def create_image_showcase_slide(img_filename, title, subtitle, duration_sec=5.0):
    frames = []
    total_frames = int(duration_sec * FPS)
    f_sub = get_font(28)
    
    img_path = os.path.join(ASSETS_DIR, img_filename)
    if os.path.exists(img_path):
        raw_img = Image.open(img_path).convert("RGB")
    else:
        raw_img = Image.new("RGB", (1200, 800), color=(30, 41, 59))
        
    # Resize keeping aspect ratio to fit inside 1300x750
    raw_img.thumbnail((1350, 800), Image.Resampling.LANCZOS)
    img_w, img_h = raw_img.size
    
    for i in range(total_frames):
        canvas = Image.new("RGB", (VIDEO_WIDTH, VIDEO_HEIGHT), color=(7, 9, 14))
        draw = ImageDraw.Draw(canvas)
        draw_header_footer(draw, title)
        
        # Paste image centered
        paste_x = (VIDEO_WIDTH - img_w) // 2
        paste_y = 100 + (VIDEO_HEIGHT - 170 - img_h) // 2
        canvas.paste(raw_img, (paste_x, paste_y))
        
        # Border
        draw.rounded_rectangle([(paste_x - 4, paste_y - 4), (paste_x + img_w + 4, paste_y + img_h + 4)], radius=8, outline=(255, 153, 0), width=3)
        
        # Subtitle callout at bottom
        draw.rectangle([(0, VIDEO_HEIGHT - 65), (VIDEO_WIDTH, VIDEO_HEIGHT)], fill=(11, 15, 25))
        draw.text((paste_x, VIDEO_HEIGHT - 50), subtitle, font=f_sub, fill=(56, 189, 248))
        
        frames.append(cv2.cvtColor(np.array(canvas), cv2.COLOR_RGB2BGR))
    return frames

def create_architecture_slide(duration_sec=4.5):
    frames = []
    total_frames = int(duration_sec * FPS)
    f_title = get_font(44, bold=True)
    f_node = get_font(28, bold=True)
    f_desc = get_font(22)
    
    for i in range(total_frames):
        img = Image.new("RGB", (VIDEO_WIDTH, VIDEO_HEIGHT), color=(7, 9, 14))
        draw = ImageDraw.Draw(img)
        draw_header_footer(draw, "AWS Builder Mini Challenge • Serverless Cloud Architecture")
        
        draw.text((120, 140), "End-to-End Multi-Modal Pipeline on AWS:", font=f_title, fill=(255, 153, 0))
        
        nodes = [
            ("1. Fire TV App", "10-Foot UI / Spatial Nav\nFire OS & Vega OS\nZero Touch Dependency", (56, 189, 248)),
            ("2. Amazon API Gateway", "REST API with CORS\nSub-50ms Routing\nSecure Token Validation", (255, 153, 0)),
            ("3. AWS Lambda", "Python 3.12 Serverless\nContext Injection\nTimestamp Bounding", (168, 85, 247)),
            ("4. Amazon Bedrock", "Converse API\nAmazon Nova Lite\nAnthropic Claude", (34, 197, 94))
        ]
        
        start_x = 120
        card_w = 360
        card_h = 280
        y = 260
        
        for idx, (n_title, n_desc, col) in enumerate(nodes):
            draw.rounded_rectangle([(start_x, y), (start_x + card_w, y + card_h)], radius=20, fill=(18, 24, 38), outline=col, width=3)
            draw.text((start_x + 25, y + 25), n_title, font=f_node, fill=col)
            draw.multiline_text((start_x + 25, y + 90), n_desc, font=f_desc, fill=(226, 232, 240), spacing=8)
            
            # Arrow
            if idx < 3:
                arrow_x = start_x + card_w + 12
                draw.text((arrow_x, y + card_h//2 - 20), "->", font=f_node, fill=(255, 255, 255))
                
            start_x += card_w + 70
            
        # Summary box
        draw.rounded_rectangle([(120, 620), (VIDEO_WIDTH - 120, 780)], radius=16, fill=(15, 23, 42), outline=(51, 65, 85), width=2)
        draw.text((160, 650), "[AWS SAM] Infrastructure as Code (template.yaml)", font=get_font(26, bold=True), fill=(255, 153, 0))
        draw.text((160, 700), "Auto-scaling concurrency via AWS Lambda | Sub-second responses on Fire TV", font=f_desc, fill=(148, 163, 184))
        
        frames.append(cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR))
    return frames

def create_outro_slide(duration_sec=4.0):
    frames = []
    total_frames = int(duration_sec * FPS)
    f_huge = get_font(64, bold=True)
    f_sub = get_font(32)
    f_info = get_font(24)
    
    for i in range(total_frames):
        img = Image.new("RGB", (VIDEO_WIDTH, VIDEO_HEIGHT), color=(7, 9, 14))
        draw = ImageDraw.Draw(img)
        
        draw.text((VIDEO_WIDTH//2 - 260, 260), "CineLens AI", font=f_huge, fill=(248, 250, 252))
        draw.text((VIDEO_WIDTH//2 - 400, 360), "The Future of Television Viewing on Amazon Fire TV", font=f_sub, fill=(255, 153, 0))
        
        draw.rounded_rectangle([(VIDEO_WIDTH//2 - 450, 480), (VIDEO_WIDTH//2 + 450, 680)], radius=20, fill=(18, 24, 38), outline=(56, 189, 248), width=2)
        draw.text((VIDEO_WIDTH//2 - 400, 520), "[x] Fire TV & Vega OS Ready (10-Foot Spatial Navigation)", font=f_info, fill=(248, 250, 252))
        draw.text((VIDEO_WIDTH//2 - 400, 570), "[x] Amazon Bedrock Converse API Integration", font=f_info, fill=(248, 250, 252))
        draw.text((VIDEO_WIDTH//2 - 400, 620), "[x] Fully Open Source with MIT License on GitHub", font=f_info, fill=(248, 250, 252))
        
        draw.text((VIDEO_WIDTH//2 - 200, 750), "Thank You For Reviewing!", font=f_sub, fill=(56, 189, 248))
        
        frames.append(cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR))
    return frames

def build_video():
    print("Generating CineLens AI Demo Video (1080p @ 30 FPS)...")
    slides = [
        create_title_slide(3.5),
        create_problem_slide(4.0),
        create_image_showcase_slide("gallery-1-hero-tv.jpg", "Fire TV 10-Foot UI - Ambient AI Slide-Over", "D-Pad remote control highlights 'Explain Scene' with live Amazon Bedrock streaming", 5.0),
        create_image_showcase_slide("gallery-2-character-recap.jpg", "Character Bios & 10-Min Spoiler-Free Recaps", "Instant actor identification, character arcs, and timestamp-bounded safe summaries", 5.0),
        create_image_showcase_slide("gallery-3-remote-navigation.jpg", "Living Room Remote Navigation", "Zero-touch, 100% directional remote control with D-pad navigation engine", 4.5),
        create_architecture_slide(4.5),
        create_outro_slide(3.5)
    ]
    
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(OUTPUT_PATH, fourcc, FPS, (VIDEO_WIDTH, VIDEO_HEIGHT))
    
    total_frames = sum(len(s) for s in slides)
    count = 0
    
    for slide in slides:
        for f in slide:
            out.write(f)
            count += 1
            if count % 150 == 0:
                print(f"  Progress: {count}/{total_frames} frames ({int(count/total_frames*100)}%)")
                
    out.release()
    print(f"Video created successfully at: {OUTPUT_PATH}")

if __name__ == "__main__":
    build_video()
