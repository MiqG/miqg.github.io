---
title: "Structure up your data science project!"
date: 2021-01-22
tags: [Data Analysis]
excerpt: "data science, project structure, workflows, reproducibility, modularity"
mathjax: true
---

# Why should I think about my project structure at all?

I spent a lot of time trying to learn and implement the “best coding practices”, but I have never really paid attention to the “best project structure practices”.

When carrying out courses or small tasks, I would never think about how I should structure the project; I would just try to tackle the question right away mixing inputs, outputs, scripts, and log files altogether.

However, as projects started gowing and new questions arose from those improvised analyses I found myself constantly having to rewrite a lot of code to make sense of the data, and feeling unsure of whether if someone asked me to re-run the analysis I would be able to do so and of getting the same results.
Indeed, during my first internship, I felt embarrassed to hand over to a colleague a project constructed following my “best chaotic practices”. I realized I needed to change this approach.

Ideally, I wanted to find the simplest project structure -and its corresponding workflow- that facilitates reproducibility and scalability. As I started googling, I noted that there were fewer resources than expected on the art of structuring data science projects. Especially applied to bioinformatics or computational biology, my main fields of interest.
Spoiler alert: I haven’t found the ideal project structure yet, but after scraping the web for more information and implementing some approaches myself, I have created a project template as a [GitHub repository](https://github.com/MiqG/project_template) that so far is doing the job for me, and I hope it works for you too. 
So far, at least having a clear project structure from the start is helping me a lot in avoiding the blank page syndrome.


# The principles: naming and modularity
To create this project template, I tried to follow two principles that the literature in best coding practices mentions a lot: clear names and modularity. 

When naming directories, their subdirectories, and files, one should try to use words that are both meaningful and that complement each other as one reads the full path of a file, for instance.

On the other hand, one should try to structure the project forcing it to grow modularly. Probably influenced by my past in the wet lab, I like to think of a project’s data analysis part as a series of experiments that try to answer a hypothesis. I try to make each experiment to answer a specific sub-question so that if we don’t need one experiment we can just delete the directory containing it, and this action will not affect the rest of the experiments. 
In those cases where an experiment’s result is the input of another experiment, the child experiment may better be introduced as a part of its parent experiment to avoid this dependency.


# The essential tools for reproducibility
As I mentioned, I would like my project to be simple and reproducible. Luckily, these properties align with the interest of a lot of people in the community, who have developed plenty of different tools on that matter. 
Among them, I find workflow and environment managers extremely useful giving us the power to re-run all our analyses automatically within the same environment. My favourite ones are the python-based workflow and environment managers: snakemake and conda.


# The basic workflow
This is an example of the basic workflow using this project structure template:

<p align="center">
	<img src="{{ site.url }}{{ site.baseurl }}/images/2021-01-22-data_science_project_template_files/project_workflow.png" width="70%"/>
</p>

1. Modify `config.yml` to your taste adding variables that could be useful project-wide.
2. Create the workflows to download and preprocess your project's data at `workflows/download/` and `workflows/preprocess`, respectively. Make sure to distinguish between code that is only used specifically for that part of the project -place it in your workflow's `scripts/` subdirectory-, or code that can be used project-wide -place it in the project's modules in `src/` and call the functions in your workflow-.
3. Now, you can analyse your data creating different experiments as subdirectories of `workflows/analyses` that will get inputs from `data/` and will output at `results/your_experiment_name/`.
4. Commit your work, and consider adding README files.
5. Inspect and explore results creating jupyter notebooks at `reports/notebooks/` that can be rendered into static web pages with [`jupyter-book`](https://jupyterbook.org/intro.html). Structure your project's book by modifying `reports/_toc.yml`.


# The structure in detail
## `data/`
```shell
data
├── prep
├── raw
└── references
```
Here we will place all the data needed for our project to be accessed easily from anywhere. The subdirectory names are self-explanatory: 
- in `raw/` we store data as it was produced experimentally or downloaded;
- in `prep/` we store raw data that has been manipulated by us in a certain manner, i.e. preprocessed, cleaned, or imputed data; and 
- in `references` we store useful “ground-truth files” or lookup tables such as, in my case, genome annotations.


## `envs/`
```shell
envs
└── main.yml
```
Working with environment managers such as conda facilitates the reproducibility of most projects seamlessly. In this directory, we place the “main.yml” project environment file containing the packages used throughout the project. We can add additional environments that certain tools might require; which can be easily activated through snakemake as we run our workflows.


## `reports/`
```shell
reports/
├── _config.yml
├── images
│   └── logo.png
├── notebooks
│   ├── example_notebook.md
│   ├── intro.md
│   └── README.md
├── README.md
└── _toc.yml
```
One of the most important and fun parts of data science is communication. For this reason, I think it is essential that every project generates a series of reports with which one tries to answer questions using the results from our analyses.
In this case, I think [jupyter-book](https://jupyterbook.org/intro.html) is a good friend because it allows us to create a simple static webpage that combines all our notebooks and can be published as a GitHub Pages like [this one](https://miqg.github.io/project_template/intro.html).


## `workflows/`
```shell
workflows/
├── analyses
│   └── new_experiment
│       ├── README.md
│       ├── run_all.sh
│       ├── scripts
│       │   └── workflow_step.py
│       └── snakefile
├── download
│   ├── README.md
│   ├── run_all.sh
│   ├── scripts
│   │   └── workflow_step.py
│   └── snakefile
├── preprocess
│   ├── README.md
│   ├── run_all.sh
│   ├── scripts
│   │   └── workflow_step.py
│   └── snakefile
└── README.md
```
This is the directory where we will spend most of our time during the project. Here, we will create our “experiments” that try to answer a specific question.

Every experiment within `workflows/analyses/` uses the files in `data/` as inputs and saves the outputs into `results/`. Exceptionally, at the beginning of the project, the workflows in `workflows/download` and `workflows/preprocess` will output into `data/raw` and `data/references` the former, and into `data/prep`, the latter.

Then, the experiments can be executed via `bash run_all.sh`, a simple script that will tell your favorite workflow manager to run the experiment with some general parameters.
Our workflow-manager script -here, the “snakefile”- contains the rules to carry out every step of our analysis. 
Finally, the `workflows/analyses/new_experiment/scripts/` subdirectory contains those scripts that carry out a specific step of that “new_experiment”.


## `results/`
```shell
results
├── new_experiment
│   ├── files
│   │   └── output_example.tsv
│   └── plots
│       └── output_example.pdf
└── README.md
```
Here we will place all the outputs from our experiments. The subdirectories in `results` should have the same name of the experiment and, in general, may contain files and plots that can be easily read from our reports.


## `src/`
```shell
src
└── python
    ├── setup.py
    └── your_project_name
        └── config.py
```
To minimize the errors that could come from copy-pasting functions or scripts across different experiments, in this directory we will create project-wide modules that can be called from anywhere in the project.
In this case, I think that one of the essential modules to have is “config.py”, which will read our top-level “config.yml” to access the variables from anywhere in the project.


# The conclusions, so far
In my empirical opinion, working with this project structure is especially helping me to focus in one thing at a time. Although it takes more time to build every step of the project I feel like these steps are solid and allow me, in the long term, to save time from all the refactoring, bug fixes, and error correction I had to do with my previous "chaotic" approaches. 

If you are reading this, you probably are interested in the topic and share the struggle in finding the project structure that best adapts to your needs. 
So, please, feel free to reach out somehow and, even better, to submit a PR and improve the [project_template](https://github.com/MiqG/project_template)!



# References
- Buffalo, V. (2015). Bioinformatics data skills: Reproducible and robust research with open source tools. " O'Reilly Media, Inc.". [link](https://www.oreilly.com/library/view/bioinformatics-data-skills/9781449367480/)
- Noble WS (2009) A Quick Guide to Organizing Computational Biology Projects. PLoS Comput Biol 5(7): e1000424. [https://doi.org/10.1371/journal.pcbi.1000424](https://doi.org/10.1371/journal.pcbi.1000424)
- [Eric Ma - Principled Data Science Workflows](https://www.youtube.com/watch?v=Dx2vG6qmtPs&ab_channel=PyData)
- [Pat Schloss - Riffomonas Project](https://www.youtube.com/channel/UCGuktEl5InrcxPfCjmPWxsA)
