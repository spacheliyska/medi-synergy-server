from gremlin_python.driver import client, serializer
from django.conf import settings

class NeptuneService:
    def __init__(self):
       self.client = client.Client(
            f"wss://{settings.NEPTUNE_HOST}:{settings.NEPTUNE_PORT}/gremlin",  # Correct connection URL
            'g', 
            username=settings.NEPTUNE_USERNAME,  # Optional
            password=settings.NEPTUNE_PASSWORD,  # Optional
            message_serializer=serializer.GraphSONSerializersV3d0()
        )
        
    def execute_query(self, query):
        try:
            # Sending the Gremlin query to Neptune
            result_set = self.client.submit(query)
            return result_set.all().result()
        except Exception as e:
            print(f"Error executing Gremlin query: {e}")
            return None
        
    def add_medication(self, medication_name, medication_type, dosage):
        query = f"""
            g.addV('Medication').property('name', '{medication_name}')
            .property('type', '{medication_type}')
            .property('dosage', '{dosage}')
        """
        return self.execute_query(query)
    
    def add_patient(self, patient_name, age):
        query = f"""
            g.addV('Patient').property('name', '{patient_name}')
            .property('age', {age})
        """
        return self.execute_query(query)

    def add_prescription(self, medication_name, patient_name):
        query = f"""
            g.V().has('Medication', 'name', '{medication_name}')
            .addE('prescribed_to')
            .to(g.V().has('Patient', 'name', '{patient_name}'))
        """
        return self.execute_query(query)

    def close_connection(self):
        self.client.close()

    def get_medication_prescriptions(self, medication_name):
        query = f"g.V().has('Medication', 'name', '{medication_name}').out('prescribed_by').values('name')"
        result = self.execute_query(query)
        return result