# Hansen and Quinn Study Software

## About
This project is a web-based study tool for students of Introductory Greek (CLGR 101/102) at Williams College. The application is designed to help students memorize verb conjugations, noun declensions, and other grammatical forms, tailored to the vocabulary and units of the primary textbook, *Greek: An Intensive Course* by Hardy Hansen and Gerald M. Quinn.

This project was created by Lauren Hall '27 and advised by Professor Sarah Olsen.

## Features

*   **Interactive Quizzes:** Test your knowledge of Greek vocabulary and grammar with interactive quizzes.
*   **Targeted Practice:** Focus on specific grammatical categories, such as verbs, nouns, adjectives, and participles.
*   **Textbook-Aligned Content:** The vocabulary and grammatical forms are organized to correspond with the units in *Greek: An Intensive Course*.
*   **Score Tracking:** Keep track of your progress and identify areas for improvement.

## Technologies Used

*   **Backend:** Python, Django
*   **Frontend:** HTML, CSS, JavaScript
*   **Database:** SQLite

## Running the software locally

1.  **Clone the repository:**
    ```
    git clone https://github.com/lkhall/greek_project.git
    cd greek_project
    ```

2.  **Set up the virtual environment:**
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```
    pip install -r requirements.txt
    ```

4.  **Run the Django development server:**
    ```
    python greekproj/manage.py runserver
    ```

    The application will be available at `http://127.0.0.1:8000/`.

## Screenshots

Main page (nouns):
<img width="1512" height="729" alt="Screenshot 2026-10-15 at 9 41 37 AM" src="https://github.com/user-attachments/assets/eae54612-2f51-4131-be27-0c63ce931d8d" />

Error checking for nouns:
<img width="496" height="286" alt="Screenshot 2026-10-15 at 9 41 53 AM" src="https://github.com/user-attachments/assets/adcf9447-6c01-4f5f-9d01-b304baf98d70" />

Verbs:
<img width="562" height="610" alt="Screenshot 2026-10-15 at 9 42 04 AM" src="https://github.com/user-attachments/assets/9fd325b6-5507-46b6-8ea9-04bce0507afa" />

Participles:
<img width="502" height="585" alt="Screenshot 2026-10-15 at 9 42 11 AM" src="https://github.com/user-attachments/assets/637c8198-6aaa-46ad-93f6-969238988fd9" />

Adjectives:
<img width="1349" height="530" alt="Screenshot 2026-10-15 at 9 42 16 AM" src="https://github.com/user-attachments/assets/c4927e8d-4efe-45ab-8a4a-1c16576c7852" />

## Future Improvements

*   Implement user accounts to allow students to track their progress over time.
*   Add more advanced grammatical categories and vocabulary from later chapters of the textbook.
*   Develop a more sophisticated algorithm for generating quiz questions based on a student's past performance.
