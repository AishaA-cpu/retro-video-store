class model_helpers:

    def missing_requirements(self, requirements, provided_attributes):

        # customer_attributes  = {"postal_code", "name", "phone"}
        # video_attributes = {"release_date", "title", "total_inventory"}
        set_missing = requirements.difference(provided_attributes)

        if set_missing:
            missing = set_missing.pop()
            return missing
        
        return None

    def makes_response(self):
        pass

    def data_not_found(self, id):
        pass

    def validate_data_id(self, id):
        pass

