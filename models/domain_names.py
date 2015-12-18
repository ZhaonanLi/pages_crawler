import MySQLdb as MySQL
import datetime


class DomainNames(object):
    def __init__(self, db_hostname, db_portnumber, db_name, db_username, db_password):
        if not db_hostname:
            raise ValueError('db hostname should not be empty')
        if db_portnumber is None and db_portnumber < 0:
            raise ValueError('db port number should be defined and valid')
        if not db_name:
            raise ValueError('db name should not be empty')
        if not db_username:
            raise ValueError('db username should not be empty')
        if not db_password:
            raise ValueError('db password should not be empty')

        self.db_hostname = db_hostname
        self.db_portnumber = db_portnumber
        self.db_name = db_name
        self.db_username = db_username
        self.db_password = db_password
        self.db = None

    def open_db_connection(self):
        self.db = MySQL.connect(host=self.db_hostname, port=self.db_portnumber, db=self.db_name,
                                user=self.db_username, passwd=self.db_password)

    def close_db_connection(self):
        if not self.db:
            self.db.close()

    def insert_domain_names(self):
        table_name = 'DomainNames'
        sql_str = 'INSERT INTO {} (domain_name, created, updated) VALUES("{}", "{}", "{}")'
        utc_timestamp = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        domain_names = [
            'nbcnews.com',
            'msn.com',
            'vice.com',
            'googleblog.blogspot.com',
            'valleywag.gawker.com',
            'businessinsider.com',
            'scobleizer.com',
            'chicagotribune.com',
            'readwrite.com',
            'slate.com',
            'wsj.com',
            'usatoday.com',
            'informationweek.com',
            'slashdot.org',
            'theinquirer.net',
            'usnews.com',
            'chron.com',
            'theregister.co.uk',
            'foxnews.com',
            'mlive.com',
            'mic.com',
            'cnn.com',
            'techgreet.com',
            'gawker.com',
            'al.com',
            'bloomberg.com',
            'macnn.com',
            'huffingtonpost.com',
            'latimes.com',
            'theblaze.com',
            'npr.org',
            'buzzfeed.com',
            'arstechnica.com',
            'dailymail.co.uk',
            'examiner.com',
            'techrepublic.com',
            'theguardian.com',
            'washingtonpost.com',
            'nypost.com',
            'pcworld.com',
            'wired.com',
            'mashable.com',
            'techspot.com',
            'cbsnews.com',
            'bits.blogs.nytimes.com',
            'bleacherreport.com',
            'independent.co.uk',
            'nj.com',
            'news.yahoo.com',
            'dallasnews.com',
            'webpronews.com',
            'time.com',
            'gigaom.com',
            'boston.com',
            'geek.com',
            'elitedaily.com',
            'techcrunch.com',
            'ilounge.com',
            'dailytech.com',
            'thedailybeast.com',
            'lifehacker.com',
            'engadget.com',
            'freep.com',
            'cnet.com',
            'venturebeat.com',
            'sfgate.com',
            'nydailynews.com',
            'upworthy.com',
            'telegraph.co.uk',
            'salon.com',
            'mirror.co.uk',
            'bgr.com',
            'bostonglobe.com',
            'i4u.com',
            'vox.com',
            'kotaku.com',
            'bbc.com',
            'theatlantic.com',
            'blog.louisgray.com',
            'gizmodo.com'
        ]

        self.open_db_connection()
        cursor = self.db.cursor()
        for domain_name in domain_names:
            sql = sql_str.format(table_name, domain_name, utc_timestamp, utc_timestamp)
            try:
                cursor.execute(sql)
                self.db.commit()
            except MySQL.Error, mysql_error:
                print mysql_error
                self.db.rollback()

        cursor.close()
        self.close_db_connection()


if __name__ == '__main__':
    print 'Program is working'

    db_hostname = '127.0.0.1'
    db_portnumber = 8889
    db_name = 'BerryBoxDB'
    db_username = 'root'
    db_password = 'root'
    domain_names_model = DomainNames(db_hostname, db_portnumber, db_name,
                                     db_username, db_password)
    domain_names_model.insert_domain_names()

    print 'Program is end'
