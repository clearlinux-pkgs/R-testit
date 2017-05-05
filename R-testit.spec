#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-testit
Version  : 0.6
Release  : 25
URL      : http://cran.r-project.org/src/contrib/testit_0.6.tar.gz
Source0  : http://cran.r-project.org/src/contrib/testit_0.6.tar.gz
Summary  : A Simple Package for Testing R Packages
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : clr-R-helpers

%description
# testit
[![Build Status](https://travis-ci.org/yihui/testit.svg)](https://travis-ci.org/yihui/testit)
[![Coverage Status](https://coveralls.io/repos/github/yihui/testit/badge.svg?branch=master)](https://coveralls.io/github/yihui/testit?branch=master)

%prep
%setup -q -c -n testit

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1492799601

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1492799601
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library testit
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library testit


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/testit/DESCRIPTION
/usr/lib64/R/library/testit/INDEX
/usr/lib64/R/library/testit/Meta/Rd.rds
/usr/lib64/R/library/testit/Meta/features.rds
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
/usr/lib64/R/library/testit/rstudio/addins.dcf
