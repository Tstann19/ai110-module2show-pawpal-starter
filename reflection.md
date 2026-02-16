# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

- Add a Pet, this class should allow the user to input pet information such as name, age, and what type of animal it is like a dog, cat, bunny, fish, etc. 

- Edit Tasks, this class should allow a user to change a current task or remove the task completely from the app.

- Create Tasks, this class should allow the user to create tasks such as walk the dog "angie" at 5:00 pm. Tasks could be to walk, feed, give medication, grooming, playtime, etc. The user should be able to determine the time as well.

- Generate Daily Plan, this class should utilize AI to generate a plan for the user to take care of their animals. 

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

---
At the start of implementation I wasn't too worried about implementing conflicts regarding time. I assumed that user could do tasks at the same time. However, once I was working on it I changed it otherwise so the schedule is cohesive. As a user, it would prove to be more helpful if the time for each task was designated to that particular task. So, later I added it into the code even though I refrained from including it earlier. 

Also the class I stated earlier to utilize AI (Generate plan) I haven't actually implemented due to it's difficulty as of yet.

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

My specific task manager considers time and priority, not necessarily preferences. I considered time to matter the most as if this must be done at a certain time that's obviously important. I assumed priority would only be taken into consideration when two or more tasks overlap. However, in my code my tasks don't overlap and will not be allowed. Even though, all tasks still have a priority considered.

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

---
One tradeoff in my application I've noticed is my application is simple and can produce reasonable plans. However, due to my code looking for the general ways a schedule can be made it misses a few
edge cases and can miss better scheduling combinations. This is reasonable as the code primarily works for majority of the part and is readable to the coder. Yet, it isn't a perfect interation of what the application could be.

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

---
I used Claude AI to help generate majority of design, and refactoring. 

I tended to keep my prompts simple and direct. This way the AI would deter ranting information that isn't what was desired. Sometimes adding "DON'T INCLUDE A DEMO" helps prevent new files of a demo that wasn't asked for.
**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---
One moment I didn't accept the AI suggestion is when the Claude AI wanted to create a complete separate file to demo a new implementation. I didn't accept this suggestion as it would over complicate my code along with the files. I had no use for a separate demo file when I have main.py and test_pawpal.py file. 

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

---
I tested primarily the features around the tasks and task manager as these were roughly much more of a complex implementation than adding pets or removing them. 

These tests were important as they were the integral part of the application. If I as an user am unable to make tasks or there was problems with that function it'd probably deter me from using the app. So, these tasks were almost required to keep the app working.

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---
I'd say roughly 4 stars that I'm confident that my scheduler works as intended. As I feel there can be more edge cases regarding time constraints. If I had more time I'd have expand more on the owner's priorities and time constraints as I was proceeding with the code became less of a priority at the time.

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

I'm most satisfied that I was able to create an application in so little time using AI. I'm also proud that I utilized files for their designated purpose. Before in coding my code felt unstructured due to the fact I didn't have practice organizing it.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

I'd probably improve the UI. To my dismay I wasn't able to give the UI more of a pop for the user so I'd probably learn how to update the UI into a better look. Such as using more color rather than black or having a more simplistic format for the user. Maybe adding tabs within the UI could also make information more easier to look at glance rather than scrolling.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?

That when utilizing AI within a project, it's important to reduce the complexity. As AI tends to complicate certain structures of code along with how files are organized as well. Also during this project I learned the types of files that come to be a structure of the system/application. Such as a diagram, test file, backend file, and specific UI file.
