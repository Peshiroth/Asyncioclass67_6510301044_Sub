#example of asyncio task group with a failed task
import asyncio

#coroutine task 
async def task1():
    #report a message
    print('Hello from coroutine 1')
    #sleep to simulate waiting
    await asyncio.sleep(1)
#coroutine task
async def task2():
    #report a message
    print('Hello from coroutine 2')
    #sleep to simulate waiting
    await asyncio.sleep(0.5)
    #fail with an expection
    raise Exception('Something Bad Happened')
async def task3():
    #report a message
    print('Hello from coroutine 3')
    #sleep to simulate waiting
    await asyncio.sleep(1)

#asyncio entry point 
async def main():
    try:
    #create task group
        async with asyncio.TaskGroup() as group:
        #run first task
            t1 = group.create_task(task1())
        #run second task
            t2 = group.create_task(task2())
        #run thrid task 
            t3 = group.create_task(task3())
    except:
        pass
    #check the status of each task
    print(f'Task1: done={t1.done()},cancelled={t1.cancelled()}')
    print(f'Task2: done={t2.done()},cancelled={t2.cancelled()}')
    print(f'Task3: done={t3.done()},cancelled={t3.cancelled()}')

asyncio.run(main())