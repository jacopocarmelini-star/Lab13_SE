from database.DB_connect import DBConnect
from model.cromosoma import Cromosoma
from model.interazione import Interazione


class DAO:

    @staticmethod
    def getCromosomi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT  cromosoma
                   FROM gene 
                WHERE cromosoma != 0"""

        cursor.execute(query)

        for row in cursor:
            cromosoma = Cromosoma(cromosoma=row["cromosoma"])
            result.append(cromosoma)

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getInterazioni(_id_map):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT g1.cromosoma as c1, g2.cromosoma as c2,  SUM(distinct(correlazione)) as somma
                    FROM gene g1, gene g2, interazione i 
                    WHERE g1.cromosoma != 0 and g2.cromosoma != 0 AND g1.cromosoma != g2.cromosoma  AND g1.id = i.id_gene1 and g2.id = i.id_gene2 
                    GROUP BY g1.cromosoma, g2.cromosoma"""

        cursor.execute(query)

        for row in cursor:
            c1 = _id_map[row["c1"]]
            c2 = _id_map[row["c2"]]
            peso = row["somma"]
            result.append(Interazione(c1, c2, peso))
        cursor.close()
        conn.close()
        return result

