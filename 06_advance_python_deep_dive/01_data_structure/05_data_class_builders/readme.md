# Data Classes

## Introduction

Data classes are like children. They are okay as a starting point, but to participate as a grownup object, they need to take some responsibility.
—Martin Fowler and Kent Beck

Python offers a few ways to build a simple class that is just a collection of fields, with little or no extra functionality. This pattern is known as a "data class." This repository covers three different class builders that you may use as shortcuts to write data classes:

## Class Builders

### 1. `collections.namedtuple`
The simplest way—available since Python 2.6.

### 2. `typing.NamedTuple`
An alternative that requires type hints on the fields—since Python 3.5, with class syntax added in 3.6.

### 3. `@dataclasses.dataclass`
A class decorator that allows more customization than previous alternatives, adding lots of options and potential complexity—since Python 3.7.

## Discussion

After covering those class builders, we will discuss why Data Class is also the name of a code smell: a coding pattern that may be a symptom of poor object-oriented design.

## Note on `typing.TypedDict`

`typing.TypedDict` may seem like another data class builder. It uses similar syntax and is described right after `typing.NamedTuple` in the typing module documentation for Python 3.9. However, `TypedDict` does not build concrete classes that you can instantiate. It’s just syntax to write type hints for function parameters and variables that will accept mapping values used as records, with keys as field names. We’ll see them in the `TypedDict` section of this repository.
