import os
import re

daily_dir = r'd:\project\my-12-week-goal\log\daily'
weekly_dir = r'd:\project\my-12-week-goal\log\weekly'

def update_daily():
    for filename in os.listdir(daily_dir):
        if filename.endswith('.md'):
            path = os.path.join(daily_dir, filename)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Update Header
            date_match = re.search(r'(\d{4})-(\d{2})-(\d{2})', content)
            if date_match and '# 📅 每日紀錄：' not in content:
                date_str = date_match.group(0)
                new_header = f'# 📅 每日紀錄：{date_str}\n\n## ⚡ 能量情緒指標：4 / 5\n\n## 📊 習慣達成狀態'
                
                # Replace old title and habit header
                content = re.sub(r'# 📔 每日生活紀錄：.*', new_header, content)
                content = re.sub(r'## 📈 核心習慣追蹤', '', content)
                
            # Update Small Summary header
            content = content.replace('## 📝 本日小結', '## 📝 本日心得小結')
            
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content.strip() + '\n')

update_daily()
print("Daily logs updated.")
