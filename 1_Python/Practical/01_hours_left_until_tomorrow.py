# hours left until tomorrow

from datetime import datetime, timedelta

now = datetime.now()
tomorrow = (now + timedelta(days=1)).replace(hour=0, minute=0, second=0, microsecond=0)
hours_left = (tomorrow - now).total_seconds() / 3600

print(f"Hours left until tomorrow: {hours_left:.2f}")
