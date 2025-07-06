# Python Katas

Kata is a Japanese word (型 or 形) meaning "form".
It refers to a detailed choreographed pattern of martial arts movements made to be practiced alone.

**Python Katas** are short, focused coding exercises designed for practice, aimed at improving specific programming skills, often involving solving problems or implementing algorithms.

## Getting started

> [!NOTE]
> To pull the new katas that don't exist in your fork, execute the following **from branch `main`**:
> 
> ```bash 
> git remote add upstream https://github.com/alonitac/PythonKatas5Tech.git
> git pull upstream main
> ```

1. **Fork** this repo, clone your forked repo and open in your preferred IDE (e.g. PyCharm).
2. Answer the exercises under `katas/`.
3. Write a corresponding unittest in `katas/test/`. The unittest test class must be named as `test_[name of kata].java`.
   For example, for the `hello_world.py` kata, the corresponding unittest must be `test_hello_world.py`.
4. You can run a single test by executing the following command from the root directory of your project: `python -m unittest katas/test/test_[name of kata].py` (change `[name of kata]` accordingly).
5. Commit and push your solutions. In you GitHub repo page, go to **Actions** and make sure you pass the automated test. 

You can enjoy a game map to see your progress: https://alonitac.github.io/PythonKatas5Tech (to load your map, enter your GitHub account, your katas repo name, and click the **Load Map** button.)


