class model_helpers:

    def missing_requirements(self, requirements, provided_attributes):
        set_missing = requirements.difference(provided_attributes)

        if set_missing:
            missing = set_missing.pop()
            return missing
        
        return None

        