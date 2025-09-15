from datetime import datetime, timedelta

class Event:
    def __init__(self, dt, name, guests, duration):
        self.dt = dt
        self.name = name
        self.guests = guests
        self.duration = duration
        self.left = None
        self.right = None

class EventBST:
    def __init__(self):
        self.root = None

    def _count_events_day(self, node, day):
        if not node:
            return 0
        count = 0
        if node.dt.date() == day:
            count += 1
        count += self._count_events_day(node.left, day)
        count += self._count_events_day(node.right, day)
        return count

    def _is_conflict(self, node, new_event):
        if not node:
            return False
        if node.dt.date() == new_event.dt.date():
            start1 = node.dt
            end1 = start1 + timedelta(hours=node.duration)
            start2 = new_event.dt
            end2 = start2 + timedelta(hours=new_event.duration)
            if abs((start1 - start2).total_seconds()) < 3 * 3600:
                return True
            if (start1 < end2 and start2 < end1):  # overlapping
                return True
        return self._is_conflict(node.left, new_event) or self._is_conflict(node.right, new_event)

    def add_event(self, dt, name, guests, duration):
        if duration > 5:
            print("Wrong Duration exceeds 5 hours.")
            return
        day = dt.date()
        if self._count_events_day(self.root, day) >= 2:
            print("Wrong Maximum 2 events allowed per day.")
            return
        new_event = Event(dt, name, guests, duration)
        if self._is_conflict(self.root, new_event):
            print("Wrong Conflict with existing event (time gap < 3 hours).")
            return
        self.root = self._insert(self.root, new_event)
        print("Yes Event added successfully.")

    def _insert(self, node, new_event):
        if not node:
            return new_event
        if new_event.dt < node.dt:
            node.left = self._insert(node.left, new_event)
        elif new_event.dt > node.dt:
            node.right = self._insert(node.right, new_event)
        return node

    def cancel_event(self, dt):
        self.root, deleted = self._delete(self.root, dt)
        if deleted:
            print("yes Event cancelled successfully.")
        else:
            print("Wrong Event not found.")

    def _delete(self, node, dt):
        if not node:
            return node, False
        deleted = False
        if dt < node.dt:
            node.left, deleted = self._delete(node.left, dt)
        elif dt > node.dt:
            node.right, deleted = self._delete(node.right, dt)
        else:
            deleted = True
            if not node.left:
                return node.right, deleted
            elif not node.right:
                return node.left, deleted
            temp = self._min_value_node(node.right)
            node.dt, node.name, node.guests, node.duration = temp.dt, temp.name, temp.guests, temp.duration
            node.right, _ = self._delete(node.right, temp.dt)
        return node, deleted

    def _min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    def display_descending(self, node=None):
        if node is None:
            node = self.root
        if node:
            self.display_descending(node.right)
            print(f"{node.dt} | {node.name} | Guests: {node.guests} | Duration: {node.duration} hrs")
            self.display_descending(node.left)

    def delete_completed(self, current_time):
        self.root = self._delete_completed(self.root, current_time)

    def _delete_completed(self, node, current_time):
        if not node:
            return None
        node.left = self._delete_completed(node.left, current_time)
        node.right = self._delete_completed(node.right, current_time)
        if node.dt + timedelta(hours=node.duration) < current_time:
            return self._delete_node(node)
        return node

    def _delete_node(self, node):
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        temp = self._min_value_node(node.right)
        node.dt, node.name, node.guests, node.duration = temp.dt, temp.name, temp.guests, temp.duration
        node.right, _ = self._delete(node.right, temp.dt)
        return node


if __name__ == "__main__":
    bst = EventBST()

    e1 = datetime(2025, 9, 15, 10, 0)
    e2 = datetime(2025, 9, 15, 15, 0)
    e3 = datetime(2025, 9, 16, 11, 0)

    bst.add_event(e1, "Conference", 100, 4)
    bst.add_event(e2, "Workshop", 50, 3)
    bst.add_event(e3, "Seminar", 200, 5)

    print("\n Events in Descending Order:")
    bst.display_descending()

    bst.cancel_event(e2)

    print("\n After Cancelling Workshop:")
    bst.display_descending()

    now = datetime(2025, 9, 16, 20, 0)
    bst.delete_completed(now)

    print("\n After Deleting Completed Events:")
    bst.display_descending()
