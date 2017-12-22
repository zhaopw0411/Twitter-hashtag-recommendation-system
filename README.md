# Bigdata-project-Hashtag-Recommendation-System
# Hashtag recommendation system using Neo4j and Apache Spark: Project Technical Instruction

In this project we leveraged the power of graph databases and built a twitter hashtag recommendation system that uses the cypher querying language that runs on Spark GraphX to provide real-time #hashtag recommendations for twitter by traversing over a large number of components. We combined graph technology and the power of Spark installed on an AWS cluster that ensuring scalability of the system.

Other Link:

Project report: *https://github.com/zhaopw0411/Twitter-hashtag-recommendation-system/blob/master/Report.pdf*  

Handout: *https://github.com/zhaopw0411/Twitter-hashtag-recommendation-system/blob/master/Handout.pdf*


## Launch a neo4j instance from AWS marketplace

Implement Neo4j Graph Database - Community Edition on AWS 

![alt text](https://github.com/zhaopw0411/Twitter-hashtag-recommendation-system/blob/master/1.png)

- Go to neo4j AWS marketplace: *https://aws.amazon.com/marketplace/pp/B071P26C9D?qid=1512270655067&sr=0-1&ref_=srh_res_product_title*

- Launch a neo4j instance from AWS marketplace

  - Set appropriate region 

  - Click continue

    ![2](https://github.com/zhaopw0411/Twitter-hashtag-recommendation-system/blob/master/2.png)


- You can use the one click launch

- Open your neo4j database on the browser. It is available at http://<amazonDNS>:7474, the original password is your instance ID

  ![alt text](https://github.com/zhaopw0411/Twitter-hashtag-recommendation-system/blob/master/3.png)


- In your command line, ssh into the neo4j database on AWS![4](C:\Users\zhaop\Google Drive\Calrson\Fall\6330 Big Data\Big data project\tech doc\4.png)
  - Login username is *ubuntu@ec2-xx-xx-xx-xx-….amazomaws.com*
  - Make sure that your private key file (*.pem*) is in the folder 

## Get Anaconda, Spark, Scala installed on Ubuntu system

- #### Download and Install Anaconda

  ```shell
  $ wget http://repo.continuum.io/archive/Anaconda3-4.1.1-Linux-x86_64.sh
  $ bash Anaconda3–4.1.1-Linux-x86_64.sh
  ```

- #### Check which Python you are using

  Ubuntu already comes with Python, but let’s make sure we are using the Anaconda version. Use:

  ```shell
  $ which python
  ```

  Most likely you won’t be using Anaconda’s version of Python (you can tell by checking the output of the which python command). Change to the Anaconda version of Python by specifying your source using:

  ```shell
  $ source .bashrc
  ```

  Then confirm with:

  ```shell
  $ which python
  ```

  Or you can just type **python** and check to see.

  #### Install Java

  Next we need to install Java in order to install Scala, which we need for Spark. Back at your EC2 command line type:

  ```
  $ sudo apt-get update
  ```

  Then install Java with:

  ```
  $ sudo apt-get install default-jre
  ```

  Check that it worked with:

  ```
  $ java -version
  ```

  #### Install Scala

  Now we can install Scala:

  ```
  $ sudo apt-get install scala
  ```

  Check that it worked with:

  ```
  $ scala -version
  ```

  (Optional: You can install specific versions of Scala with the following, just replace the version numbers):

  ```
  $ wget http://www.scala-lang.org/files/archive/scala-2.11.8.deb
  ```

  ```
  $ sudo dpkg -i scala-2.11.8.deb
  ```

  #### Install py4j

  We need to install the python library py4j, in order to this we need to make sure that pip install is connected to our Anaconda installation of Python instead of Ubuntu’s default. In the console we will export the path for pip:

  ```shell
  $ export PATH=$PATH:$HOME/anaconda3/bin
  ```

  Then use conda to install pip:

  ```shell
  $ conda install pip
  ```

  Confirm that the correct pip is being used with:

  ```shell
  $ which pip
  ```

  Now we can install py4j with pip:

  ```shell
  $ pip install py4j
  ```

  #### Install Spark and Hadoop

  Use the following to download and install Spark and Hadoop:

  ```
  $ wget http://archive.apache.org/dist/spark/spark-2.0.0/spark-2.0.0-bin-hadoop2.7.tgz
  ```

  ```
  $ sudo tar -zxvf spark-2.0.0-bin-hadoop2.7.tgz
  ```

  #### Tell Python where to find Spark

  Finally we need to set our Paths for Spark so Python can find it:

  ```shell
  $ export SPARK_HOME='/home/ubuntu/spark-2.0.0-bin-hadoop2.7'
  $ export PATH=$SPARK_HOME:$PATH
  $ export PYTHONPATH=$SPARK_HOME/python:$PYTHONPATH
  ```

  Reference: *https://medium.com/@josemarcialportilla/getting-spark-python-and-jupyter-notebook-running-on-amazon-ec2-dec599e1c297*

- #### Configure Jupyter Notebook on Your EC2 Instance

  You can follow the instruction in the link: http://docs.aws.amazon.com/mxnet/latest/dg/setup-jupyter-configure-server.html

  **Configure the Jupyter server**

  1. Create an SSL certificate.

     ```shell
     $ cd
     $ mkdir ssl
     $ cd ssl
     $ sudo openssl req -x509 -nodes -days 365 -newkey rsa:1024 -keyout "cert.key" -out "cert.pem" -batch
     ```

  2. Create a password. You use this password to log in to the Jupyter notebook server from your client so you can access notebooks on the server.

     1. Open the iPython terminal.

        ```shell
        $ ipython
        ```

        At the iPython prompt, run the `passwd()`command to set the password.

        ```shell
        CopyiPythonPrompt> from IPython.lib import passwd 
        iPythonPrompt> passwd() 
        ```

        You get the password hash (For example,`sha1:examplefc216:3a35a98ed...`).

     2. Record the password hash.

     3. Exit the iPython terminal.

        ```shell
        $ exit
        ```

  3. Create a Jupyter configuration file.

     ```shell
     $ jupyter notebook --generate-config 
     ```

     The command creates a configuration file (`jupyter_notebook_config.py`) in the `~/.jupyter` directory.

  4. Update the configuration file to store your password and SSL certificate information.

     1. Open the .config file.

        ```shell
        $ vi ~/.jupyter/jupyter_notebook_config.py
        ```

     2. Paste the following text at the end of the file. You will need to provide your password hash.

        ```shell
        c = get_config()  # Get the config object.
        c.NotebookApp.certfile = u'/home/ubuntu/ssl/cert.pem' # path to the certificate we generated
        c.NotebookApp.keyfile = u'/home/ubuntu/ssl/cert.key' # path to the certificate key we generated
        c.IPKernelApp.pylab = 'inline'  # in-line figure when using Matplotlib
        c.NotebookApp.ip = '*'  # Serve notebooks locally.
        c.NotebookApp.open_browser = False  # Do not open a browser window by default when using notebooks.
        c.NotebookApp.password = 'sha1:fc216:3a35a98ed980b9...'  
        ```

        This completes Jupyter server configuration.


- #### Configure the Client to Connect to the Jupyter Server

  You can follow the instruction in the link: http://docs.aws.amazon.com/mxnet/latest/dg/setup-jupyter-configure-client-windows.html

  To connect your Windows client to the Jupyter server, do the following:

  - Configure proxy settings

    Configure your Internet browser to use an add-on, such as FoxyProxy, to manage your Socket Secure (SOCKS) proxy settings. The proxy management add-on enables you to limit the proxy settings to domains that match the form of the public DNS name of your EC2 instance. The add-on automatically handles turning the proxy on and off when you switch between viewing websites hosted on the EC2 instance and those on the Internet.

  - Set up an SSH tunnel to your EC2 instance

    This is also known as port forwarding. If you create the tunnel using dynamic port forwarding, all traffic that is routed to a specified unused local port is forwarded to the Jupyter server on the EC2 instance. This creates a SOCKS proxy.

    **Configure Browser Proxy Settings**(**Configure proxy settings for Chrome**)

    1. Download and install the Standard version of FoxyProxy from Chrome Extension store and use pre-defined patterns and priorities:

       ![alt text](https://github.umn.edu/zhao0885/Bigdata-project-Hashtag-Recommendation-System/blob/master/Capture.PNG)

       ![alt text](https://github.umn.edu/zhao0885/Bigdata-project-Hashtag-Recommendation-System/blob/master/Capture2.PNG)

    2. Using a text editor, create a file named`foxyproxy-settings.xml`. Save the following to the file:

       ```
       <?xml version="1.0" encoding="UTF-8"?>
       <foxyproxy>
          <proxies>
             <proxy name="ec2-socks-proxy" id="2322596116" notes="" fromSubscription="false" enabled="true" mode="manual" selectedTabIndex="2" lastresort="false" animatedIcons="true" includeInCycle="true" color="#0055E5" proxyDNS="true" noInternalIPs="false" autoconfMode="pac" clearCacheBeforeUse="false" disableCache="false" clearCookiesBeforeUse="false" rejectCookies="false">
                <matches>
                   <match enabled="true" name="*ec2*.amazonaws.com*" pattern="*ec2*.amazonaws.com*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" />
                   <match enabled="true" name="*ec2*.compute*" pattern="*ec2*.compute*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false" />
                   <match enabled="true" name="*.compute.internal*" pattern="*.compute.internal*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false"/>
                   <match enabled="true" name="*.ec2.internal* " pattern="*.ec2.internal*" isRegEx="false" isBlackList="false" isMultiLine="false" caseSensitive="false" fromSubscription="false"/>
       	  </matches>
                <manualconf host="localhost" port="8157" socksversion="5" isSocks="true" username="" password="" domain="" />
             </proxy>
          </proxies>
       </foxyproxy>
       ```

       You use these settings file in the next step when configuring FoxyProxy. The settings do the following:

       - Port 8157 is the local port number used to establish the SSH tunnel with the Jupyter server. This must match the port number you used in PuTTY or in the terminal.
       - The * *ec2* * *.amazonaws.com* pattern matches the public DNS name of clusters in AWS US Regions.
       - The * *ec2* *.compute* pattern matches the public DNS name of clusters in all other AWS Regions.

    3. Configure FoxyProxy.

       1. Choose **Customize and Control Google Chrome**, choose **Tools** (or **More Tools**), and then choose **Extensions**.

       2. Next to **FoxyProxy Standard**, choose **Options**.

       3. Choose **Extensions**, choose **Options**, and then do the following.

          1. Import the settings file.

             On the **Import/Export** page, choose**Choose File**, and then open the`foxyproxy-settings.xml` file that you saved in the preceding step. If you are prompted to overwrite the settings, do so.

          2. Choose **Proxy mode**, and then choose **Use proxies based on their predefined patterns and priorities**.


- #### Set Up an SSH Tunnel to Your EC2 Instance on the Client

  Your client uses an SSH tunnel to your EC2 instance for dynamic port forwarding. For Windows, we use a PuTTY SSH client. First download and install PuTTY and PuTTYgen tools. For more information, see [PuTTY download page](http://www.chiark.greenend.org.uk/~sgtatham/putty/).

  **Note**

  You need both the PuTTY and PuTTYgen tools. PuTTY does not natively support the key-pair private key file format (.pem) generated by Amazon Elastic Compute Cloud (Amazon EC2). You use PuTTYgen to convert your key file to the required PuTTY format (.ppk). Convert your key into this format (.ppk) before attempting to connect to the master node using PuTTY. For more information about converting your key, see [Connecting to Your Linux Instance from Windows Using PuTTY](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html) in the *Amazon EC2 User Guide for Linux Instances*.

  **Set up an SSH tunnel using dynamic port forwarding on Windows**

1. Start PuTTY by double-clicking `putty.exe`.

2. In the **Categories** section, choose **Sessions** and for **Host Name**, type **ubuntu@MasterPublicDNS**. For example:

   ```shell
   ubuntu@ec2-##-###-###-###.compute-1.amazonaws.com
   ```

3. In the **Categories** section, choose **Connection**. Choose **SSH**, and then choose **Auth**.

4. For **Private key file for authentication**, choose **Browse**, and then choose the `.ppk` file.

5. In the **Categories** section, choose **Connection-**. Choose **SSH**, and then choose **Tunnels**. Configure the tunnel.

   1. For **Source port**, type **8157** (an unused local port).
   2. Choose **Dynamic** and **Auto**.
   3. Choose **Add**, and then choose **Open**.

   This opens the tunnel.

6. Create a directory on the EC2 instance for storing Jupyter notebooks. This is your Jupyter workspace.

   ```shell
   $ mkdir ~/mynotebooks
   $ cd ~/mynotebooks
   ```

## Install Apache Toree

Run the following code to install Apache Toree in your bash

```shell
#!/bin/bash
pip install -i https://pypi.anaconda.org/hyoon/simple toree
jupyter toree install --spark_home=$SPARK_HOME --user #will install scala + spark kernel
jupyter toree install --spark_home=$SPARK_HOME --interpreters=PySpark --user ubuntu
jupyter kernelspec list
jupyter notebook #launch jupyter notebook
```

## Start the Jupyter notebook server

```shell
$ jupyter notebook
```

By default, the server runs on port 8888. If the port is not available, it uses the next available port. The Jupyter terminal shows the port on which the server is listening. Now you are able to connect neo4j and spark together and write queries on Jupyter note book.

![alt text](https://github.com/zhaopw0411/Twitter-hashtag-recommendation-system/blob/master/Capture22.PNG)

## Parse Tweets and upload to AWS Neo4J database

There are multiple ways to get twitter data, for example:

- Use Spark Streaming 

- Use TwitterR package in R 

- Use Tweepy package in python

  ...

Also there are multiple approach to import data Into Neo4j, you can get more information from here: https://neo4j.com/developer/guide-importing-data-and-etl/

- Use TwitterR package in R 
- Import the Data using Cypher
- Use super Fast Batch Importer For huge datasets

Here we will provide a method to help you easily get some tweets importing into neo4j: run the R code in ' Neo4j Creating Graph Code.rmd', you will get your sample data ready on AWS neo4j database.

Open neo4j browser on port 7474, now you can play with your graph database!



![alt text](https://github.com/zhaopw0411/Twitter-hashtag-recommendation-system/blob/master/Capture6.PNG)

## Query from Apache Spark using Scala

- Launch Jupyter from Putty and now on the Jupyter notebook, you can query from your neo4j database

![alt text](https://github.com/zhaopw0411/Twitter-hashtag-recommendation-system/blob/master/WhatsApp%20Image%202017-12-04%20at%207.28.43%20PM.jpeg)
