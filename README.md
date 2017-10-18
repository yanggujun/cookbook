### bash color

    Black        0;30     Dark Gray     1;30

    Red          0;31     Light Red     1;31

    Green        0;32     Light Green   1;32

    Brown/Orange 0;33     Yellow        1;33

    Blue         0;34     Light Blue    1;34

    Purple       0;35     Light Purple  1;35

    Cyan         0;36     Light Cyan    1;36

    Light Gray   0;37     White         1;37
    
    no color     

And then use them like this in your script:

```bash
  echo -e "I \033[0;31mlove\033[0m github"
```


### vim
```
    # run commands on each line
    :<startline>,<endline>norm <vim commands>
    
    # change case of the whole word
    g~iw
    
    # split horizontally
    :split
    
    # split vertically
    :vsplit
    
    # replace a with b in the file
    :%s/a/b/g
    
    # replace a with b in a range
    :<startline>,<endline>s/a/b/g
```
