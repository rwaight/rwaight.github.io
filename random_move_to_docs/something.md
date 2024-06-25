# Random notes that should be organized

# Random MacOS Notes

#### MacOS Accounts

https://osxdaily.com/2016/07/05/list-user-accounts-command-line-mac/


## List User Accounts on Mac from Command Line

Title: **List User Accounts on Mac from Command Line**
From https://osxdaily.com/2016/07/05/list-user-accounts-command-line-mac/

Jul 5, 2016 - 19 Comments

Mac administrators may find themselves in a situation where they need to display a list of all user accounts on a particular Mac by way of the command line. We’ll review a few methods for advanced individuals to list all accounts, both user and system, on any Mac with any version of Mac OS X system software.

A few preliminary basic approaches to this would be to access the login screen or to list the contents of the /Users directory, though if a [user account is hidden](https://osxdaily.com/2015/02/01/hide-specific-user-account-mac-os-x/) then it would not display at the login screen and it’s equally simple to obfuscate a user from the /Users folder. Additionally, the existence of a name in the /Users/ directory is not foolproof, because you can delete a user account but preserve that users home directory. As a result, while those approaches may be appropriate for the casual Mac user looking to show what users they have on a computer, neither of those methods are particularly sufficient for most admin needs. But, by turning to the command line you can reveal all user accounts on a Mac, whether they are general user accounts of active users, admin accounts, as well as any system account.


### How to List All User Accounts on a Mac from Command Line

Open the Terminal if you haven’t done so already, either on the local machine you want to list user accounts for, or by connecting to a remote Mac you’d like to see the user accounts on. We’ll then use the ‘dscl’ command, which works in all versions of Mac OS X system software.


#### View All Users & Accounts on a Mac

```bash
dscl . list /Users
```

The benefit (or trouble) with this approach is that it lists not only all user accounts on a Mac but it also shows every daemon and server process account. This would include usernames like Paul, Bob, Jill, but also daemons, system accounts, and process users like networkd, windowserver, daemon, nobody, root, _spotlight, _ard, _appserver, _iconservices, and many more.

If the complete list of users is thus undesirable, you can easily exclude all the _underscore daemon and process accounts by running the output through grep, as we’ll show next.


#### Show User Accounts Only

```bash
dscl . list /Users | grep -v '_'
```

This command will filter out any of the _ underscore prefixed daemon users, which are not actually user accounts. You’ll get a much shorter list of user names returned as a result, but you’ll still find three user names included that are not typical user accounts, but are normal to be found on Mac OS X installs; daemon, nobody, and root.


#### Show All User Accounts, User Directories, & User GECOS Info on a Mac

Another approach would be to show and list a detailed account list of user accounts, the associated user account directory, and the user account GECOS info (which is usually a description of the account or a full user name). If you find yourself wondering what on earth some of the system accounts and process user ID accounts in the aforementioned lists are, this approach offers more details, including the gecos description for each account (for example, _qtss user is the QuickTime Streaming Server daemon)
```bash
dscacheutil -q user
```

The output of that command will be rather extensive, so you may want to pipe the result through more or less or redirect it into a text file for easier parsing.

There are likely other means of displaying all user accounts on a Mac, regardless of system version, if you know of an effective of informative method not covered here, do share it in the comments.

## How to Hide a Specific User Account from Login Screens of Mac OS X

Title: **How to Hide a Specific User Account from Login Screens of Mac OS X**
From: https://osxdaily.com/2015/02/01/hide-specific-user-account-mac-os-x/

# next random section

# End of page