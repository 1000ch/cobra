import flask
from cobra import app
from cobra.subscriptions import Subscriptions
from cobra.entry import EntryDAO


@app.route('/')
def show_entries():

    # dao
    entry_dao = EntryDAO()

    # get entries from db
    entries = entry_dao.findall()
    feeds = []
    for entry in entries:
        if not entry['feedTitle'] in feeds:
            feeds.append(entry['feedTitle'])

    #top_entries = entry_dao.find({}, 0, 20)

    return flask.render_template('index.html', entries = entries, feeds = feeds)

@app.route('/update')
def update_entries():

    # get feeds
    feeds = Subscriptions('cobra/static/subscriptions.xml').get_feeds()

    # connect to db
    entries = []
    for feed in feeds:
        for entry in feed.entries:
            entries.append({
                'feedTitle': feed.title,
                'htmlUrl': feed.htmlUrl,
                'xmlUrl': feed.xmlUrl,
                'title': entry.title,
                'link': entry.link,
                'date': entry.date
            })

    entry_dao = EntryDAO()
    entry_dao.clear()
    entry_dao.insert(entries)
    entry_dao.index()

    return flask.redirect('/')

@app.route('/clear')
def clear_entries():
    entry_dao = EntryDAO()
    entry_dao.clear()

    return flask.redirect('/')