from flask import Flask, render_template, request, url_for, redirect, flash, abort, jsonify
import sqlite3

app = Flask(__name__)

connection = sqlite3.connect("stats.db", check_same_thread=False)
print(connection.total_changes)

cursor = connection.cursor()
# ["Rock", "Paper", "Scissors", "Spock", "Lizard"]

cursor.execute("CREATE TABLE IF NOT EXISTS stats (id INTEGER, player TEXT, rock INTEGER, paper INTEGER, "
               "scissors INTEGER, spock INTEGER, lizard INTEGER)")

connection.commit()


@app.route('/saveStat', methods=['POST'])
def insert_new_entry_to_db():
    data = request.get_json()
    if not data:
        return abort(404)

    nickname = data.get('nickname')
    rock = data.get('rock')
    paper = data.get('paper')
    scissors = data.get('scissors')
    spock = data.get('spock')
    lizard = data.get('lizard')

    cursor.execute("INSERT INTO stats (player, rock, paper, scissors, spock, lizard) VALUES (?, ?, ?, ?, ?, ?)",
                   (nickname, rock, paper, scissors, spock, lizard))
    connection.commit()

    return jsonify({'message': 'Entry added successfully'})


@app.route('/getStats', methods=['GET'])
def read_database():
    cursor.execute("SELECT * FROM stats")
    connection.commit()
    rows = cursor.fetchall()
    stats = [{'player': row[1], 'rock': row[2], 'paper': row[3], 'scissors': row[4], 'spock': row[5], 'lizard': row[6]}
             for row in rows]
    return jsonify({'stats': stats})


if __name__ == '__main__':
    app.run(debug=True)

'''
url = "http://url.com"
query = {„field“: value}
res = resuests.post(url, data=query)
print(res.text)
'''
