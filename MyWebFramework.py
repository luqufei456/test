def one(self, sql, params=[]):
    try:
        self.open()
        self.cursor.execute(sql, params)
        result = self.cursor.fetchone()
        self.close()
        return result

    except Exception as e:
        print(e)