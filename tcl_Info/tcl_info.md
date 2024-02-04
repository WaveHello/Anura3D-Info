# Information on Coding in tcl

When writing tcl code there needs to be a space between the end of the condition curlys and the execution curlys ie.

**This is good**
Notice the space between ```"hello"}``` and ```{```
```tcl
if{$variable == "hello"} {
    Do something here
}
```

**:warning: :warning: This is bad :warning: :warning:**
There's no space. This will give you error after bracket or something like that
```tcl
if{$variable == "hello"}{
    Do something here
}

```tcl
|| # - This is how you write a logical "or"
&& # - This is how you write logical "and"
```
# Using with GiD

Gid has a in house debugger for tcl that is extremly helpful when modifying the GiD problem type scripts.
[Video: How to use GiD debugger](https://www.youtube.com/watch?v=G98cmhN8Jzk)