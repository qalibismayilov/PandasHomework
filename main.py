import pandas as pd

books = {
    "Title": [
        "The Alchemist",
        "1984",
        "Atomic Habits",
        "The Hobbit",
        "Clean Code",
        "The Great Gatsby"
    ],
    "Author": [
        "Paulo Coelho",
        "George Orwell",
        "James Clear",
        "J.R.R. Tolkien",
        "Robert Martin",
        "F. Scott Fitzgerald"
    ],
    "PublicationYear": [
        1988,
        1949,
        2018,
        1937,
        2008,
        1925
    ],
    "Price": [
        15,
        20,
        25,
        18,
        30,
        12
    ]
}

df_books = pd.DataFrame(books)

print(df_books)
average_price = df_books["Price"].mean()

print("Orta qiymet:", average_price)
new_books = df_books[df_books["PublicationYear"] > 2015]

print(new_books)
sorted_books = df_books.sort_values("Price")

print(sorted_books)
orders = pd.read_csv("orders.csv")

print(orders)
print(orders.head(10))
customer_orders = orders["Customer"].value_counts()

print(customer_orders)
max_amount = orders["Amount"].max()
min_amount = orders["Amount"].min()

print("Maksimum Amount:", max_amount)
print("Minimum Amount:", min_amount)
total_amount = orders["Amount"].sum()

print("Umumi mebleg:", total_amount)
food = {
    "Product": [
        "Pizza",
        "Burger",
        "Chicken",
        "Rice",
        "Salad",
        "Pasta",
        "Steak",
        "Sandwich",
        "Fish",
        "Oatmeal"
    ],
    "Category": [
        "Fast Food",
        "Fast Food",
        "Meat",
        "Grain",
        "Vegetable",
        "Fast Food",
        "Meat",
        "Fast Food",
        "Seafood",
        "Grain"
    ],
    "Calories": [
        500,
        650,
        400,
        350,
        180,
        550,
        700,
        450,
        320,
        250
    ],
    "Protein": [
        20,
        25,
        35,
        8,
        5,
        18,
        45,
        20,
        30,
        10
    ]
}

df_food = pd.DataFrame(food)
print(df_food)
high_calories = df_food[df_food["Calories"] > 300]

print(high_calories)
average_protein = df_food.groupby("Category")["Protein"].mean()

print(average_protein)
sorted_food = df_food.sort_values("Calories", ascending=False)

print(sorted_food)
employees = {
    "Name": [
        "Ali",
        "Veli",
        "Hasan",
        "Ali",
        "Veli",
        "Hasan",
        "Murad",
        "Murad"
    ],
    "Project": [
        "Website",
        "Mobile App",
        "Website",
        "Database",
        "Database",
        "Mobile App",
        "Website",
        "Mobile App"
    ],
    "Hours": [
        20,
        30,
        25,
        15,
        20,
        35,
        40,
        25
    ]
}

df_employees = pd.DataFrame(employees)
print(df_employees)
total_hours_name = df_employees.groupby("Name")["Hours"].sum()

print(total_hours_name)
total_hours_project = df_employees.groupby("Project")["Hours"].sum()

print(total_hours_project)
top_employee = total_hours_name.idxmax()
top_hours = total_hours_name.max()

print("En cox saat isleyen emekdas:", top_employee)
print("Umumi saat:", top_hours)
tickets = {
    "Movie": [
        "Avatar",
        "Batman",
        "Avatar",
        "Titanic",
        "Batman",
        "Titanic",
        "Avatar",
        "Joker",
        "Batman",
        "Joker",
        "Titanic",
        "Avatar"
    ],
    "City": [
        "Baku",
        "Baku",
        "Ganja",
        "Baku",
        "Ganja",
        "Sumqayit",
        "Sumqayit",
        "Baku",
        "Sumqayit",
        "Ganja",
        "Ganja",
        "Baku"
    ],
    "TicketsSold": [
        100,
        150,
        80,
        120,
        90,
        110,
        130,
        160,
        70,
        100,
        95,
        140
    ]
}

df_tickets = pd.DataFrame(tickets)
print(df_tickets)
movie_tickets = df_tickets.groupby("Movie")["TicketsSold"].sum()

print(movie_tickets)
city_tickets = df_tickets.groupby("City")["TicketsSold"].sum()

print(city_tickets)
top_movie = movie_tickets.idxmax()
top_movie_tickets = movie_tickets.max()

print("En cox bilet satilan film:", top_movie)
print("Bilet sayi:", top_movie_tickets)