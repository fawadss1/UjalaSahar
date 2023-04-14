(function ($) {
    'use strict';
    function setCookie(key, value) {
        const expires = new Date();
        expires.setTime(expires.getTime() + (value * 24 * 60 * 60 * 1000));
        document.cookie = key + '=' + value + ';expires=' + expires.toUTCString() + '; SameSite=Strict;path=/';
    }
    function getCookie(key) {
        const keyValue = document.cookie.match('(^|;) ?' + key + '=([^;]*)(;|$)');
        return keyValue ? keyValue[2] : null;
    }

    function handleMenu() {
        $('[data-widget=pushmenu]').bind('click', function () {
            const menuClosed = getCookie('jazzy_menu') === 'closed';
            if (!menuClosed) {
                setCookie('jazzy_menu', 'closed');
            } else {
                setCookie('jazzy_menu', 'open');
            }
        });
    }

    function setActiveLinks() {
        const url = window.location.pathname;
        const $breadcrumb = $('.breadcrumb a').last();
        const $link = $('a[href="' + url + '"]');
        const $parent_link = $('a[href="' + $breadcrumb.attr('href') + '"]');

        if ($link.length) {
            $link.addClass('active');
        } else if ($parent_link.length) {
            $parent_link.addClass('active');
        }

        const $a_active = $('a.nav-link.active');
        const $main_li_parent = $a_active.closest('li.nav-item.has-treeview');
        const $ul_child = $main_li_parent.children('ul');

        $ul_child.show();
        $main_li_parent.addClass('menu-is-opening menu-open');
    }

    $(document).ready(function () {
        setActiveLinks()
        handleMenu();
        const $changeListTable = $('#changelist .results table');
        if ($changeListTable.length && !$changeListTable.hasClass('table table-striped')) {
            $changeListTable.addClass('table table-striped');
        }
    });

})(jQuery);
$(".main-footer > .float-right").text('Developed By Fawad').css('font-weight', 'bold');
$(".brand-text").text('').addClass('ml-4');
