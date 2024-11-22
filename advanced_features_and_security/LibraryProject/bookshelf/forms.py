<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form Example</title>
</head>
<body>
    <h1>Submit Book Information</h1>
    <form method="POST" action="{% url 'bookshelf:submit_book' %}">
        {% csrf_token %}
        <label for="title">Book Title:</label>
        <input type="text" id="title" name="title" required><br><br>
        
        <label for="author">Author:</label>
        <input type="text" id="author" name="author" required><br><br>
        
        <button type="submit">Submit</button>
    </form>
</body>
</html>
