def test_application_message():
   message = b"Hello from version 2 of my Dockerized Python application!"
   assert b"Dockerized Python application" in message