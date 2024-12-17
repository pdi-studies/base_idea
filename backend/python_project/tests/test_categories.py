import unittest
from flask import Flask
from app import create_app, db
from api.model.category import Category


class TestCategories(unittest.TestCase):
    def setUp(self):
        self.app = create_app() 
        self.client = self.app.test_client()
        self.app_context = self.app.app_context()
        self.app_context.push()

        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_categories(self):
        response = self.client.get('/api/categories')

        self.assertEqual(response.status_code, 200)

        data = response.get_json()
        self.assertIsInstance(data, list)

        expected_years = [
            {"id": 1, "category_type": 'bird', "title": 'Passarinhos', "icon": "<svg xmlns='http://www.w3.org/2000/svg' width='1em' height='1em' viewBox='0 0 256 256'><path fill='currentColor' d='M176 68a12 12 0 1 1-12-12a12 12 0 0 1 12 12m64 12a8 8 0 0 1-3.56 6.66L216 100.28V120a104.11 104.11 0 0 1-104 104H24a16 16 0 0 1-12.49-26l.1-.12L96 96.63V76.89c0-33.42 26.79-60.73 59.71-60.89h.29a60 60 0 0 1 57.21 41.86l23.23 15.48A8 8 0 0 1 240 80m-22.42 0L201.9 69.54a8 8 0 0 1-3.31-4.64A44 44 0 0 0 156 32h-.22C131.64 32.12 112 52.25 112 76.89v22.63a8 8 0 0 1-1.85 5.13L24 208h26.9l70.94-85.12a8 8 0 1 1 12.29 10.24L71.75 208H112a88.1 88.1 0 0 0 88-88V96a8 8 0 0 1 3.56-6.66Z'/></svg>", "active": True},
            {"id": 2, "category_type": 'dog', "title": 'Cachorrinhos', "icon": "<svg xmlns='http://www.w3.org/2000/svg' width='1em' height='1em' viewBox='0 0 256 256'><path fill='currentColor' d='m239.71 125l-16.42-88a16 16 0 0 0-19.61-12.58l-.31.09L150.85 40h-45.7L52.63 24.56l-.31-.09a16 16 0 0 0-19.61 12.58L16.29 125a15.77 15.77 0 0 0 9.12 17.52a16.3 16.3 0 0 0 6.71 1.48a15.5 15.5 0 0 0 7.88-2.16V184a40 40 0 0 0 40 40h96a40 40 0 0 0 40-40v-42.15a15.5 15.5 0 0 0 7.87 2.16a16.3 16.3 0 0 0 6.72-1.47a15.77 15.77 0 0 0 9.12-17.54M32 128l16.43-88L90.5 52.37Zm144 80h-40v-12.69l13.66-13.65a8 8 0 0 0-11.32-11.32L128 180.69l-10.34-10.35a8 8 0 0 0-11.32 11.32L120 195.31V208H80a24 24 0 0 1-24-24v-60.89L107.92 56h40.15L200 123.11V184a24 24 0 0 1-24 24m48-80l-58.5-75.63L207.57 40zm-120 12a12 12 0 1 1-12-12a12 12 0 0 1 12 12m72 0a12 12 0 1 1-12-12a12 12 0 0 1 12 12'/></svg>", "active": True},
            {"id": 3, "category_type": 'fish', "title": 'Peixinhos', "icon": "<svg xmlns='http://www.w3.org/2000/svg' width='1em' height='1em' viewBox='0 0 256 256'><path fill='currentColor' d='M168 76a12 12 0 1 1-12-12a12 12 0 0 1 12 12m48.72 67.64c-19.37 34.9-55.44 53.76-107.24 56.1l-22 51.41A8 8 0 0 1 80.1 256h-.51a8 8 0 0 1-7.19-5.78l-14.8-51.83l-51.8-14.83a8 8 0 0 1-1-15.05l51.41-22c2.35-51.78 21.21-87.84 56.09-107.22c24.75-13.74 52.74-15.84 71.88-15.18c18.64.64 36 4.27 38.86 6a8 8 0 0 1 2.83 2.83c1.69 2.85 5.33 20.21 6 38.85c.68 19.1-1.41 47.1-15.15 71.85m-55.18 29a52.11 52.11 0 0 1-33.4-44.78a52.09 52.09 0 0 1-44.77-33.39q-10.45 23.79-11.3 57.59a8 8 0 0 1-4.85 7.17l-35.39 15.14l34.45 9.86a8 8 0 0 1 5.49 5.5l9.84 34.44l15.16-35.4a8 8 0 0 1 7.17-4.84q33.77-.81 57.6-11.29m50.88-129.07c-14.15-3-64.1-11-100.3 14.75a81.2 81.2 0 0 0-16 15.07a36 36 0 0 0 39.35 38.44a8 8 0 0 1 8.73 8.73a36 36 0 0 0 38.47 39.34a80.8 80.8 0 0 0 15-16c25.75-36.17 17.75-86.16 14.75-100.33'/></svg>", "active": True},
            {"id": 4, "category_type": 'cat', "title": 'Gatinhos', "icon": "<svg xmlns='http://www.w3.org/2000/svg' width='1em' height='1em' viewBox='0 0 256 256'><path fill='currentColor' d='M96 140a12 12 0 1 1-12-12a12 12 0 0 1 12 12m76-12a12 12 0 1 0 12 12a12 12 0 0 0-12-12m60-80v88c0 52.93-46.65 96-104 96S24 188.93 24 136V48a16 16 0 0 1 27.31-11.31c.14.14.26.27.38.41L69 57a111.22 111.22 0 0 1 118.1 0l17.21-19.9c.12-.14.24-.27.38-.41A16 16 0 0 1 232 48m-16 0l-21.56 24.8a8 8 0 0 1-10.81 1.2A89 89 0 0 0 168 64.75V88a8 8 0 1 1-16 0V59.05a97.4 97.4 0 0 0-16-2.72V88a8 8 0 1 1-16 0V56.33a97.4 97.4 0 0 0-16 2.72V88a8 8 0 1 1-16 0V64.75A89 89 0 0 0 72.37 74a8 8 0 0 1-10.81-1.17L40 48v88c0 41.66 35.21 76 80 79.67v-20.36l-13.66-13.66a8 8 0 0 1 11.32-11.31L128 180.68l10.34-10.34a8 8 0 0 1 11.32 11.31L136 195.31v20.36c44.79-3.69 80-38 80-79.67Z'/></svg>", "active": True},
        ]
        self.assertEqual(data, expected_years)


if __name__ == '__main__':
    unittest.main()
