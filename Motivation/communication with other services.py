class GamificationManager:
    def award_badge(self, user_id: int, badge_type: str) -> bool:
        """Выдача значка за активность."""
        pass

    def update_leaderboard(self, user_id: int) -> dict:
        """Обновление рейтинга."""
        pass

class NotificationManager:
    def send_deadline_reminder(self, user_id: int) -> bool:
        """Напоминание о дедлайне."""
        pass

    def toggle_notifications(self, user_id: int, is_enabled: bool) -> bool:
        """Настройка уведомлений."""
        pass

class SocialIntegration:
    def share_achievement(self, user_id: int, platform: str) -> bool:
        """Публикация достижений в соцсетях."""
        pass