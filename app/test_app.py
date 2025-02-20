from flask import current_app # Flask instance of the API

def test_app_page():
    response = current_app.test_client().get('/<name>')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Testing, Flask!'
