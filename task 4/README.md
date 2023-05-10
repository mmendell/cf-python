Why is file storage important when you’re using Python? What would happen if you didn’t store local files?

  it allows you to store data ad retrieve, enabling you to recover data beyond the runtime of your program. in addition it can allow you to share data between programs.

  in additon it eases data handling and efficiency allowing you to access large amounts of data without overloading your memory use


In this Exercise you learned about the pickling process with the pickle.dump() method. What are pickles? In which situations would you choose to use pickles and why? 

  allows you to serialize data to be stored in a binary file for later access. connects to the benefits of storing local files. its an ideal way to store large amounts of data.
  

In Python, what function do you use to find out which directory you’re currently in? What if you wanted to change your current working directory?

  current_directory = os.getcwd()
  print("Current directory:", current_directory)

  new_directory = "/path/to/new/directory"
  os.chdir(new_directory)

Imagine you’re working on a Python script and are worried there may be an error in a block of code. How would you approach the situation to prevent the entire script from terminating due to an error?

  by using an except and try block
