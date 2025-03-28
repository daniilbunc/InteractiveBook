class UserManager:
    def register(self, email: str, password: str, social_auth: dict = None) -> bool:
        """Регисbтрация через почту или соцсети."""
        pass

    def login(self, email: str, password: str) -> bool:
        """Вход в систему."""
        pass

    def update_profile(self, user_id: int, photo: str, name: str, role: str) -> bool:
        """Обновление данных профиля."""
        pass

class SecurityManager:
    def encrypt_password(self, password: str) -> str:
        """Шифрование пароля."""
        pass

    def backup_data(self, user_id: int) -> bool:
        """Резервное копирование."""
        pass

class AccessibilityManager:
    def set_font_size(self, user_id: int, size: str) -> bool:
        """Настройка шрифта."""
        pass

    def toggle_dark_mode(self, user_id: int) -> bool:
        """Включение тёмной темы."""
        pass