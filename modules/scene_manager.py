# scene_manager.py
class SceneManager:
    def __init__(self):
        self.known_ids = set()

    def analyze(self, tracked_objects):
        current_ids = set(obj['track_id'] for obj in tracked_objects)
        new_objects = current_ids - self.known_ids
        missing_objects = self.known_ids - current_ids
        self.known_ids = current_ids

        return list(new_objects), list(missing_objects)
