from neo4j import GraphDatabase, basic_auth
import sys

password = "neo"

query = """\
MERGE (p1:Person {name: $person1 })
MERGE (p2:Person {name: $person2 })
MERGE (p1)-[:KNOWS]->(p2)
"""

def import_data(person1, person2):
    with GraphDatabase.driver("bolt://localhost:7687", auth=basic_auth("neo4j", password)) as driver:
        with driver.session() as session:
            result = session.run(query, {"person1": person1, "person2": person2})
            print(result.consume().counters);

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python import.py name1 name2")
        sys.exit(1)

    import_data(sys.argv[1], sys.argv[2])
