# Postmortem
----------------------------------
### Issue Summary:
* Start-time:
06/May/2022 2:17 PM (GMT) End-time: 06/May/2022 3:07 PM (GMT)

* what was the impact:
the internal website used by the sales team to track customer interactions doesn't work.

* what was the root cause:
processes are stuck waiting for the operating system to return from system calls.

-----------------------------------
### Timeline
* when was the issue detected:

	2:17 PM (GMT)

* how was the issue detected


	2:20 PM (GMT) a user complained that they can't see the sales system's landing page

* actions taken

	2:22 PM (GMT) The issue was sent to the IT support team to troubleshoot it

	2:23 PM (GMT) A reproduction case was created to make sure it's not a user computer issue.

	2:24 PM (GMT) A few quick checks were run to verify if the problem is isolated to that specific website or not like other internal websites were checked like the inventory website or ticketing system were working okay

	2:27 PM (GMT) The server was checked using the **top** command which shows the state of the computer processes using the most CPU and to see that the computer is super overloaded.  The load average in the first line says 40, which shows most of the CPU time is

	3:00 PM (GMT) Looking at the list of processes, it shows that the backup system is running on the same server.

	3:03 PM (GMT) The backup system is killed

	3:05 PM (GMT) **top** command is run again, the load is going down and process is not longer waiting.

	3:07 PM (GMT) The website logged in and landing page is working.
-----------------------------------------------

* Root cause and resolution must contain:

	The backup process was on the same server where the website is hosted, which used most of the cpu, so it's on waiting stage.
	The issue was solved by killing the backup process in that server.

-----------------------------------------------

* Corrective and preventative measures must contain:

	Make sure that the backing up system should on a separate server so it wont overload and website stops working.
	
	To-do:
	
	 Create a backup process in different server.
