The standard Amazon Linux image often comes with outdated versions of packages like CMake. The default package repository often does not have newer versions. While this problem is often solved using containers, there is a small niche audience that needs to eliminate dependencies and runtime complexity and would prefer to run natively on Amazon Linux itself. You can use this repository directly as source input into AWS CodeBuild to build a RPM package that you can redistribute and install on your Amazon Linux instances (using `yum` or `dnf`). 

# Reommendations
Due to the bespoke nature of everyone's build processes, it is recommended that you fork and make tweaks that best align with your needs. There is no guarantee of backwards compatability for future changes.
