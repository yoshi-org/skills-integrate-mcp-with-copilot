import unittest
from http.cookies import SimpleCookie

from fastapi import HTTPException, Response

from app import (
    LoginRequest,
    activities,
    auth_status,
    login,
    require_teacher,
    signup_for_activity,
    teacher_sessions,
    unregister_from_activity,
)


class TeacherAuthenticationTests(unittest.TestCase):
    def setUp(self):
        teacher_sessions.clear()

    def tearDown(self):
        teacher_sessions.clear()

    def test_anonymous_user_cannot_authenticate(self):
        with self.assertRaises(HTTPException) as context:
            require_teacher(None)

        self.assertEqual(context.exception.status_code, 401)

    def test_invalid_credentials_are_rejected(self):
        with self.assertRaises(HTTPException) as context:
            login(LoginRequest(username="teacher", password="wrong"), Response())

        self.assertEqual(context.exception.status_code, 401)

    def test_login_creates_an_authenticated_session(self):
        response = Response()

        result = login(
            LoginRequest(username="teacher", password="mergington2026"),
            response,
        )

        cookies = SimpleCookie()
        cookies.load(response.headers["set-cookie"])
        session_token = cookies["session_token"].value
        self.assertEqual(result, {"username": "teacher"})
        self.assertEqual(require_teacher(session_token), "teacher")
        self.assertEqual(
            auth_status(session_token),
            {"authenticated": True, "username": "teacher"},
        )

    def test_teacher_can_register_and_unregister_student(self):
        activity_name = "Chess Club"
        email = "auth-test@mergington.edu"

        signup_for_activity(activity_name, email, "teacher")
        self.assertIn(email, activities[activity_name]["participants"])

        unregister_from_activity(activity_name, email, "teacher")
        self.assertNotIn(email, activities[activity_name]["participants"])


if __name__ == "__main__":
    unittest.main()