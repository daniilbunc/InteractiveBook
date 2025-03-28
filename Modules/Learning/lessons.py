class CourseManager:
    def create_course(self, title: str, description: str) -> int:
        """Создание курса."""
        pass

    def add_lesson(self, course_id: int, video_url: str, text: str) -> int:
        """Добавление урока."""
        pass

class AssignmentManager:
    def submit_test(self, user_id: int, answers: dict) -> float:
        """Отправка теста с автоматической проверкой."""
        pass

    def submit_code(self, user_id: int, code: str) -> str:
        """Проверка кода."""
        pass

class ProgressTracker:
    def get_progress(self, user_id: int) -> dict:
        """Отслеживание пройденных уроков."""
        pass

    def get_recommendations(self, user_id: int) -> list:
        """Рекомендации по повторению."""
        pass

class DiscussionManager:
    def post_question(self, user_id: int, lesson_id: int, text: str) -> int:
        """Задать вопрос к уроку."""
        pass

    def moderate_message(self, message_id: int) -> bool:
        """Модерация сообщений."""
        pass