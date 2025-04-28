# tracker.py
from deep_sort_realtime.deepsort_tracker import DeepSort

class ObjectTracker:
    def __init__(self):
        self.tracker = DeepSort(max_age=30)  # adjust for how long to remember

    def update(self, detections):
        track_inputs = [
            (det['bbox'], det['confidence'], det['class']) for det in detections
        ]
        tracks = self.tracker.update_tracks(track_inputs, frame=None)
        tracked = []
        for track in tracks:
            if not track.is_confirmed():
                continue
            bbox = track.to_ltrb()  # [x1, y1, x2, y2]
            tracked.append({
                'track_id': track.track_id,
                'bbox': bbox,
                'class': track.get_class()
            })
        return tracked
