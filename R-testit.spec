#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-testit
Version  : 0.4
Release  : 4
URL      : http://cran.r-project.org/src/contrib/testit_0.4.tar.gz
Source0  : http://cran.r-project.org/src/contrib/testit_0.4.tar.gz
Summary  : A Simple Package for Testing R Packages
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : clr-R-helpers

%description
# testit
[![Build Status](https://travis-ci.org/yihui/testit.svg)](https://travis-ci.org/yihui/testit)

%prep
%setup -q -c -n testit

%build

%install
rm -rf %{buildroot}
export LANG=C
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library testit
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library testit


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/testit/DESCRIPTION
/usr/lib64/R/library/testit/INDEX
/usr/lib64/R/library/testit/Meta/Rd.rds
/usr/lib64/R/library/testit/Meta/hsearch.rds
/usr/lib64/R/library/testit/Meta/links.rds
/usr/lib64/R/library/testit/Meta/nsInfo.rds
/usr/lib64/R/library/testit/Meta/package.rds
/usr/lib64/R/library/testit/NAMESPACE
/usr/lib64/R/library/testit/NEWS
/usr/lib64/R/library/testit/R/testit
/usr/lib64/R/library/testit/R/testit.rdb
/usr/lib64/R/library/testit/R/testit.rdx
/usr/lib64/R/library/testit/help/AnIndex
/usr/lib64/R/library/testit/help/aliases.rds
/usr/lib64/R/library/testit/help/paths.rds
/usr/lib64/R/library/testit/help/testit.rdb
/usr/lib64/R/library/testit/help/testit.rdx
/usr/lib64/R/library/testit/html/00Index.html
/usr/lib64/R/library/testit/html/R.css
