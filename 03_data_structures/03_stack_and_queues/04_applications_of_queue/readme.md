#  **Queues: Media Player Example** 🎵

## � Table of Contents
- [**Queues: Media Player Example** 🎵](#queues-media-player-example-)
  - [� Table of Contents](#-table-of-contents)
  - [�📚 Real-World Use Cases of Queues](#-real-world-use-cases-of-queues)
  - [🎵 Media Player Queue Example](#-media-player-queue-example)
    - [1️⃣ The Track Class](#1️⃣-the-track-class)
    - [2️⃣ The MediaPlayerQueue Class](#2️⃣-the-mediaplayerqueue-class)
    - [3️⃣ The Play Function](#3️⃣-the-play-function)
    - [4️⃣ Complete Example: Play a Playlist](#4️⃣-complete-example-play-a-playlist)
  - [Key points 🚀](#key-points-)

---

## �📚 Real-World Use Cases of Queues

Queues are used to implement many functionalities in real computer applications:

* **Printer Queues:**
  On a network, multiple computers can share one printer. Print jobs are **queued**; the printer handles jobs in the order they arrive (FIFO).

* **CPU Scheduling:**
  Operating systems queue processes to be executed by the CPU, ensuring fair and orderly processing.

* **Music/Media Player Playlists:**
  Tracks are played in the order added to the playlist (FIFO). When you hit play, each song is played sequentially.

## 🎵 Media Player Queue Example

Let’s create a simple music player playlist using queues!

### 1️⃣ The Track Class

Each **Track** has a title and a random length (between 5 and 10 seconds):

```python
from random import randint

class Track:
    def __init__(self, title=None):
        self.title = title
        self.length = randint(5, 10)
```

**Example Usage:**

```python
track1 = Track("white whistle")
track2 = Track("butter butter")
print(track1.length)
print(track2.length)
```

*Output might be:*

```
6
7
```

*(Values may vary due to randomness)*

### 2️⃣ The MediaPlayerQueue Class

We inherit from the `Queue` class (linked list implementation):

```python
import time

class MediaPlayerQueue(Queue):
    def add_track(self, track):
        self.enqueue(track)
```

* `add_track` simply enqueues the track object into the queue.

### 3️⃣ The Play Function

Plays all tracks in the queue, **in order**:

```python
def play(self):
    while self.count > 0:
        current_track_node = self.dequeue()
        print("Now playing {}".format(current_track_node.data.title))
        time.sleep(current_track_node.data.length)
```

* The player keeps playing until the queue is empty.
* Each track is **dequeued** (removed from front), its title printed, and the program pauses for the length of the track.


### 4️⃣ Complete Example: Play a Playlist

```python
track1 = Track("white whistle")
track2 = Track("butter butter")
track3 = Track("Oh black star")
track4 = Track("Watch that chicken")
track5 = Track("Don't go")

print(track1.length)
print(track2.length)
# (Print lengths for demo)

media_player = MediaPlayerQueue()
media_player.add_track(track1)
media_player.add_track(track2)
media_player.add_track(track3)
media_player.add_track(track4)
media_player.add_track(track5)
media_player.play()
```

*Sample Output:*

```
8
9
Now playing white whistle
Now playing butter butter
Now playing Oh black star
Now playing Watch that chicken
Now playing Don't go
```

* Each song is played **in the order added** (FIFO).
* Each "Now playing ..." message is followed by a pause for the track’s duration.

##  Key points 🚀

* Queues are **perfect** for managing tasks in order (print jobs, process scheduling, media playlists).
* **FIFO**: First item in, first item out.
* In this music player, tracks are played exactly in the order they are added to the queue.
