import heapq
from typing import List

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Input: har task = [enqueueTime, processingTime]
        # enqueueTime = task kab CPU ki line me aayega (available kab hoga)
        # processingTime = task kitni der chalega (duration)

        # Output: indices ka order jisme CPU tasks execute karega.

        # Rules:
        # 1) CPU idle hai aur koi available task nahi -> CPU idle rahega.
        # 2) CPU free hote hi, available tasks me se pick karo:
        #    - minimum processingTime wala
        #    - tie ho to smaller index wala
        # 3) Agar ek task start ho gaya, beech me preempt nahi kar sakte
        #    (task complete hoga tabhi next choose hoga).

        n = len(tasks)

        # Step 1: original index attach karo, because sort karne se indices lost ho jaate hain
        # Ab format: (enqueueTime, processingTime, index)
        tasks = [(tasks[i][0], tasks[i][1], i) for i in range(n)]

        # Step 2: tasks ko enqueueTime ke basis pe sort karo
        # Taaki hum timeline me left-to-right scan kar sakein
        tasks.sort()

        # Min-heap for "available tasks"
        # Heap key: (processingTime, index)
        # Because hume hamesha shortest duration task chahiye; tie me smaller index
        minHeap = []

        res = []      # final order of indices
        time = 0      # current time on CPU timeline
        i = 0         # pointer in sorted tasks list

        # Main loop:
        # Condition: ya to tasks remaining ho (i < n) OR heap me pending tasks ho
        while i < n or minHeap:

            # Agar heap empty hai, matlab CPU idle hai,
            # aur next task future me aayega, to time ko jump kar do
            if not minHeap and time < tasks[i][0]:
                time = tasks[i][0]

            # Step 3: jitne tasks ka enqueueTime <= current time, unko heap me push karo
            # Matlab: jo tasks "line me aa chuke" hain, unko available pool me daal do
            while i < n and tasks[i][0] <= time:
                enqueue, proc, idx = tasks[i]
                heapq.heappush(minHeap, (proc, idx))  # (duration, index)
                i += 1

            # Step 4: heap se best task pop karo
            # Best = smallest processingTime, tie -> smallest index
            proc, idx = heapq.heappop(minHeap)

            # Step 5: CPU ye task run karega for "proc" time (no interruption)
            time += proc

            # Step 6: answer me index add karo (execution order)
            res.append(idx)

        return res