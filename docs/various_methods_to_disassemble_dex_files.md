---
tags:
  -  Howtos
---
This how-to documents various methods and tools in disassembling DEX
files for the Android OS. An example "Hello Android"
[APK](apk.md) file developed from the Android SDK example is
used to demonstrate the various tools. The various tools and methods are
listed below in the subsections.

## Tools

The HelloAndroid.apk package was decompressed using a standard
zip-utility. The output from the zip utility produced the following
files:

    $unzip HelloAndroid.apk
    Archive:  HelloAndroid.apk
      inflating: res/layout/main.xml
      inflating: AndroidManifest.xml
     extracting: resources.arsc
     extracting: res/drawable-hdpi/icon.png
     extracting: res/drawable-ldpi/icon.png
     extracting: res/drawable-mdpi/icon.png
      inflating: classes.dex

The file of importance in analyzing the various methods of disassembly
is 'classes.dex'. The various tools listed below will use this file.

### dedexer

A disassembler (available at <http://dedexer.sourceforge.net/>) to turn
the DEX format into an "assembly-like format". The format uses Jasmin
like syntax and various Dalvik opcodes. The command used to disassemble
the classes.dex file is:

    $ java -jar ddx1.11.jar -d HelloAndroidOoutput classes.dex
    Processing com/example/helloandroid/HelloAndroid
    Processing com/example/helloandroid/R$attr
    Processing com/example/helloandroid/R$drawable
    Processing com/example/helloandroid/R$layout
    Processing com/example/helloandroid/R$string
    Processing com/example/helloandroid/R

The command produced several files, but the important file is located at
com/example/helloandroid/HelloAndroid. The disassembly listing for that
file is below.

    $ cat com/example/helloandroid/HelloAndroid.ddx
    .class public com/example/helloandroid/HelloAndroid
    .super android/app/Activity
    .source HelloAndroid.java

    .method public <init>()V
    .limit registers 1
    ; this: v0 (Lcom/example/helloandroid/HelloAndroid;)
    .line 7
            invoke-direct   {v0},android/app/Activity/<init>        ; <init>()V
            return-void
    .end method

    .method public onCreate(Landroid/os/Bundle;)V
    .limit registers 4
    ; this: v2 (Lcom/example/helloandroid/HelloAndroid;)
    ; parameter[0] : v3 (Landroid/os/Bundle;)
    .line 11
            invoke-super    {v2,v3},android/app/Activity/onCreate   ; onCreate(Landroid/os/Bundle;)V
    .line 12
            new-instance    v0,android/widget/TextView
            invoke-direct   {v0,v2},android/widget/TextView/<init>  ; <init>(Landroid/content/Context;)V
    .line 13
            const-string    v1,"Hello, Android"
            invoke-virtual  {v0,v1},android/widget/TextView/setText ; setText(Ljava/lang/CharSequence;)V
    .line 14
            invoke-virtual  {v2,v0},com/example/helloandroid/HelloAndroid/setContentView    ; setContentView(Landroid/view/View;)V
    .line 15
            return-void
    .end method

### baksmali

The baksmali disassembler (available at
<http://code.google.com/p/smali/>) disassembles the DEX file into a
format loosely based on the Jasmin's/dedexer's syntax. The command used
in this analysis to generate the disassembly is:

    $ java -jar baksmali-1.2.4.jar classes.dex

The command outputs several files and produces the
/out/com/example/helloandroid directory structure, but the main file to
investigate is HelloAndroid.smali. HelloAndroid.smali displays the
Jasmin syntax and partial Dalvik opcodes as:

    .class public Lcom/example/helloandroid/HelloAndroid;
    .super Landroid/app/Activity;
    .source "HelloAndroid.java"


    # direct methods
    .method public constructor <init>()V
        .registers 1

        .prologue
        .line 7
        invoke-direct {p0}, Landroid/app/Activity;-><init>()V

        return-void
    .end method


    # virtual methods
    .method public onCreate(Landroid/os/Bundle;)V
        .registers 4
        .parameter "savedInstanceState"

        .prologue
        .line 11
        invoke-super {p0, p1}, Landroid/app/Activity;->onCreate(Landroid/os/Bundle;)V

        .line 12
        new-instance v0, Landroid/widget/TextView;

        invoke-direct {v0, p0}, Landroid/widget/TextView;-><init>(Landroid/content/Context;)V

        .line 13
        .local v0, tv:Landroid/widget/TextView;
        const-string v1, "Hello, Android"

        invoke-virtual {v0, v1}, Landroid/widget/TextView;->setText(Ljava/lang/CharSequence;)V

        .line 14
        invoke-virtual {p0, v0}, Lcom/example/helloandroid/HelloAndroid;->setContentView(Landroid/view/View;)V

        .line 15
        return-void
    .end method

### dex2jar

An easier method for disassembling DEX files is to reproduce the Java
files. The procedure for performing this task is to take the Dalvik
opcodes to the Java byte codes (JAR file). The next step is to take a
Java decompiler, which will produce several java files. The two tools
used in the section are dex2jar (available at
<http://code.google.com/p/dex2jar/>) and a java decompiler of choice.
The steps performed to complete this transformation are:

1.  $ ./dex2jar.bat classes.dex

2.  Load the produced JAR file from dex2jar into the java decompiler.

The main class produced from the decompilation process using dex2jar is
listed below.

    package com.example.helloandroid;

    import android.app.Activity;
    import android.os.Bundle;
    import android.widget.TextView;

    public class HelloAndroid extends Activity
    {
      public void onCreate(Bundle paramBundle)
      {
        super.onCreate(paramBundle);
        TextView localTextView = new TextView(this);
        localTextView.setText("Hello, Android");
        setContentView(localTextView);
      }
    }

