# CLPsych 2021 Shared Task

Despite years of research seeking to understand risk factors and improve prevention, suicide remains a leading cause of death worldwide [[1][owid],[2][franklin2017]]. Recent work using NLP and machine learning approaches shows strong potential to help, particularly in its ability to tap into the everyday thoughts, feelings, and experiences of individuals by looking at their activity on social media [[3][coppersmith2018],[4][ophir2020]]. However, data connected with mental health is sensitive and difficult to obtain, and lack of community-level access to shared datasets is an obstacle to progress.

The 2021 Workshop on Computational Linguistics and Clinical Psychology ([CLPsych 2021](https://clpsych.org)) will be held on June 11 in conjunction with [NAACL 2021](https://2021.naacl.org/).
For the CLPsych 2021 Shared Task, we have created an opportunity for secure and ethical access to sensitive data in order to work as a community on the problem of predicting suicide risk from social media. The dataset for the task includes de-identified Twitter posts and ground-truth outcomes from individuals who have attempted or succeeded in a suicide attempt, along with control individuals who have not; these data were donated for research purposes at [OurDataHelps][odh]. Teams participating in the shared task will do their experimentation on the [UMD/NORC Mental Health Data Enclave](#data-access-enclave), a secure computing environment that brings researchers to the data rather than vice-versa.

Resources in support of this task are being provided by Qntfy (which runs [OurDataHelps][odh] and is providing the dataset), NORC at the University of Chicago (which operates the [UMD/NORC Mental Health Data Enclave](#data-access-enclave)), and by Amazon (which has contributed AWS computing credits via an Amazon Machine Learning Research Award). 

## Quick Links

 - Register your team for the shared task: [form][register]
   *(Note: Note that we may need to impose a cap on the number of teams that can participate.)*
 - Register each team member of your team: [form](https://docs.google.com/forms/d/e/1FAIpQLSe43xvI1pcPHjMIL28MeCp2IU7j02u_l_ljEmHl7A03tQsClA/viewform?usp=sf_link)
   - In addition, each team member must send an email to [the task organizers][contact-us with subject line "CLPsych shared task: <team_name>" with the following PDF attachments:
   - NORC Non-disclosure: [form](https://github.com/seanmacavaney/clpsych2021-shared-task/raw/main/clpsych2021_NORC_nondisclosure_agreement.pdf)
   - NORC DUA: [form](https://raw.githubusercontent.com/seanmacavaney/clpsych2021-shared-task/main/norc_dua.pdf)
 - Google Group: [clpsych-2021-shared-task][googlegroup]
 - Contact task organizers: [email][contact-us]
<!-- - Contact Enclave: ... TODO-->
<!-- - Submit results: ... TODO-->
<!-- - Submit system description paper: ... TODO-->

## Timeline

 - **26 Feb 2021** - Task announced and [registration open][register]
 -  **1 Mar 2021** - Availability of training data and Enclave.
                     Note that you need to submit DUA before access to
                     Enclave is available.
 - **31 Mar 2021** - System submissions due. (11:59pm AOE)
 -  **1 Apr 2021** - Results announced.
 -  **8 Apr 2021** - System description papers due.
 - **15 Apr 2021** - Acceptance notification.
 - **23 Apr 2021** - Camera ready due.

## Data

Teams will work on the Enclave with social media data donated by people who attempted suicide or loved ones of those lost to suicide at [OurDataHelps.org][odh]. As discussed below, teams will also have access to a [Practice Dataset](#practice-data) that can be used at their own sites for development and debugging.

### Data Format

The data are provided in in JSON-lines files (one for train and one for test), where 
each line represents a single user and their tweets. The format is as follows:

```python
{
	"id": str, # anonymized user ID- used for submission
	"label": bool, # 1 for users with a known attempt, 0 for control (in the practice dataset: true for depression hashtag, false for control)
	"date_of_attempts": [str], # the known dates of attempts
	"tweets": [
		{
			"id": str,
			"text": str,
			"created_at": str
		}
	]
}
```

Naturally, the `date_of_attempts` fields are not available in
the test set.

### Data Access (Enclave)

After signing a Data Use Agreement with NORC, participating teams will be given login credentials on the UMD/NORC Mental Health Data Enclave. Access to the Enclave is accomplished via a secure desktop client the participant will install locally. From their desktop, participants will be able to log in to a well-outfitted AWS EC2 instance allocated for their use. (Each team will be allocated a generous allowance of AWS credits that should be sufficient for participating in the shared task.) Within the Enclave on the desktop and AWS environment, no copying of data out of the environment is possible (not even via copy/paste). 

To avoid wasting AWS credits while designing your systems, we recommend
using the [Practice Dataset](#practice-data).

Detailed information about access to the Enclave, the computing environment, available packages and resources, support, etc., will be provided to teams when they receive their login credentials. 


### Scoring and Submission Format

The official task metrics are F1 score, F2 score (weights recall higher than
precision), True Positive Rate, False Alarm Rate, and AUC. We provide our
official scoring script here: [scoring script][score-script]. The script
takes in the source file and a TSV file with your results. The TSV file
should be formatted as follows:

```
[USER_ID] \t [LABEL] \t [SCORE]
```

Where `USER_ID` is the ID field from the source file, `LABEL` is either `1` for suicide
or `0` for control, and `SCORE` is a real-valued score output score from your system,
where larger numbers indicate the `SUICIDE` class and lower numbers indicate
`CONTROL`. The scores allow us to compute AUC and ROC curves, whereas the
label specifies the particular operating point you choose for your submission.



### Practice Data

We provide a practice dataset to help build your system outside of the enclave. This
practice dataset is based on a modified version of [swcwang/depression-detection][dd].
The task is to identify users who have tweeted with a #depression (or similar) hashtag.

Note that although we performed spot checks to make sure this dataset seems reasonable,
the practice dataset has **not** been validated by the community, so results from it
should be approached with skepticism.

More information about using the Practice Dataset is found [here](https://github.com/seanmacavaney/clpsych2021-shared-task/tree/main/practice-dataset)

### Baseline System

We provide a baseline system [here][baseline]. You are free to use or build
upon this system as you wish.

### Additional Data

We will also be making a copy of the [UMD Reddit Suicidality Dataset][umdreddit] available on the Enclave, in case some teams wish to make use of it, e.g. for feature selection or transfer learning. Because you will only have access to this dataset on the secure Enclave as part of the shared task, you will *not* be required to go through the standard application and approval process (e.g. obtaining your own organization's IRB approval). (Teams are also welcome to go through the standard application process at any time to get a copy of the Reddit Suicidality Dataset on their own site; see *How to Request Access* on the dataset page linked above.)

## Publication

All shared task participants will have the opportunity to contribute a short
system description paper for inclusion in the official workshop proceedings. Note that the
timeline, particularly for paper writing/reviewing/revision, is quite
compressed, because we want to provide shared task participants with an
official publication in the workshop proceedings and we have been given a
strict, unmovable deadline by the conference organizers for sending final
camera-ready shared task papers.

## Organizers

 - [Sean MacAvaney](https://macavaney.us/) (University of Glasgow, Georgetown University)
 - [Anjali Mittu](https://anjali.mittudev.com/) (University of Maryland)
 - [Philip Resnik](http://users.umiacs.umd.edu/~resnik/) (University of Maryland)

You can contact the organizers [here][contact-us]


[contact-us]: mailto:clpsych-2021-shared-task-organizers@googlegroups.com
[owid]: https://ourworldindata.org/suicide
[odh]: https://ourdatahelps.org/
[register]: https://forms.gle/A9S5Qq7UcDY8CEMp9
[dd]: https://github.com/swcwang/depression-detection
[score-script]: https://github.com/anjmittu/clpsych2021-shared-task-baseline/blob/master/risk_model/evaluation.py
[baseline]: https://github.com/anjmittu/clpsych2021-shared-task-baseline
[googlegroup]: https://groups.google.com/g/clpsych-2021-shared-task
[franklin2017]: https://nocklab.fas.harvard.edu/files/nocklab/files/franklin_2016_riskfactors_metaanal50_psychbull.pdf
[coppersmith2018]: https://search.proquest.com/docview/2168011772
[ophir2020]: https://www.nature.com/articles/s41598-020-73917-0
[umdreddit]:https://umiacs.umd.edu/~resnik/umd_reddit_suicidality_dataset.html
