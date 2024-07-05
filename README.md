# Linux Bash Scripting

Watch Chapter 2 and 3: https://www.linkedin.com/learning/learning-bash-scripting-17063287 

Let’s say if I want to download all the images from the langara website that we retrieved
from the previous section, we can run the wget command  on every file above, like this: 

![wget example](images/intro2.gif)

I got tired typing after 2 downloads, lol.

There is a better way, basically we want to run the command:

```
curl -s https://langara.ca | grep -o -E '/_files.*jpg'
```

We store the output into an array variable, then we want to run wget on every item of the array.
This is how we can do it via a shell script, a program that uses shell commands.
Here is the code:

```
# Stores the output into the array call FILES
# NOTE: we use command substitution $( ) to capture the 
# output of a command into a variable
FILES=$(curl -s https://langara.ca | grep -o -E '/_files.*jpg')

# Loop over the FILES array.  In bash, assigning we need
# to prefix a variable with the $ sign to access its content
for F in $FILES
do
    # we are inside the loop, and we can now run wget on
    # the $F variable.  Noticed the use of variable expansion ${}
    wget https://langara.ca${F}
done
```

Save this in a file called download.sh and we can run it using the command

```
bash download.sh
```

To make the file easier to run, we can make the file executable.  To do this,
we need to first add a line in the beginning of the file to indicate to Linux
that this file requires the bash program.
This is generally called the **shebang** line:

```
#!/bin/bash

# Stores the output into the array call FILES
# NOTE: we use command substitution $( ) to capture the 
# output of a command into a variable
FILES=$(curl -s https://langara.ca | grep -o -E '/_files.*jpg')

# Loop over the FILES array.  In bash, assigning we need
# to prefix a variable with the $ sign to access its content
for F in $FILES
do
    # we are inside the loop, and we can now run wget on
    # the $F variable.  Noticed the use of variable expansion ${}
    wget https://langara.ca${F}
done
```

We then change the permission of the file so it is executable by Linux,
finally we can run it on the command line:

![running script directly](images/intro1.gif)

Notice that we have to provide the path to the current directory when calling the script
file.

# Question 1

Follow the instructions above and complete the **download.sh** file.

# Notes

1. Use the -P option of grep if you want to use the standard regex that you learned last week.
i.e.

![grep -P](images/image1.gif)

2. If you would like to have syntax highlighting on your bash terminal, copy the following 2
files from my home directory to yours, then exit and re-login:

```
cp /home/jmadar/.bashrc ${HOME}
cp /home/jmadar/.profile ${HOME}
```

3. A reminder that to make your script file executable, you need to do the following:

  - Add the `#!/bin/bash` line as the first line of your script
  - Run `chmod +x ${script_filename}` to give the file executable permission
  - Execute the file by calling it directly (with path), i.e.
  ```
  ./${script_filename}
  ```








