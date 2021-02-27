#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	More routines for operating on iterables, beyond itertools
Summary(pl.UTF-8):	Uzupełniające itertools dodatkowe funkcje do operowania na zmiennych iterowalnych
Name:		python3-more_itertools
Version:	8.1.0
Release:	2
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/more-itertools/
Source0:	https://files.pythonhosted.org/packages/source/m/more_itertools/more-itertools-%{version}.tar.gz
# Source0-md5:	a552b06cec1bdf01d60f952dbcc9a021
URL:		https://github.com/erikrose/more-itertools
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python's itertools library is a gem - you can compose elegant
solutions for a variety of problems with the functions it provides. In
more-itertools we collect additional building blocks, recipes, and
routines for working with Python iterables.

%description -l pl.UTF-8
Biblioteka Pythona itertools to skarb - przy użyciu udostępnianych
funkcji można komponować eleganckie rozwiązania różnych problemów.
W pakiecie more-itertools zebrane są dodatkowe elementy konstrukcyjne,
przepisy i procedury do pracy z pythonowymi zmiennymi iterowalnymi.

%package apidocs
Summary:	API documentation for Python more-itertools module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona more-itertools
Group:		Documentation

%description apidocs
API documentation for Python more-itertools module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona more-itertools.

%prep
%setup -q -n more-itertools-%{version}

%build
%py3_build

%if %{with tests}
%{__python3} -m unittest discover -s tests
%endif

%if %{with doc}
PYTHONPATH=$(pwd) \
%{__make} -C docs html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%{py3_sitescriptdir}/more_itertools
%{py3_sitescriptdir}/more_itertools-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/{_modules,_static,*.html,*.js}
%endif
